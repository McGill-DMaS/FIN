import subprocess
import json
from elftools.elf.elffile import ELFFile
from compare_binaries import compare
from tqdm import tqdm
import argparse
from pathlib import Path
import os


def run_ida_script(ida_path, binary):
    
    status = 0
    current_directory = os.path.abspath(os.getcwd())
    script_path = os.path.join(current_directory, "fin/disassemble.py")
    command = [ida_path, '-A', '-B', f'-S{script_path}', f'{binary}']
    
    try:
        result = subprocess.run(command, check=True, shell=True)
        status = 1
    except subprocess.CalledProcessError as e:
        print(f"Error:{e}")
        status = 0
        

    return status


def dump_debug_line(elf_file_path, addr_mapping):
    with open(elf_file_path, 'rb') as f:
        elffile = ELFFile(f)
        dwarfinfo = elffile.get_dwarf_info()
        
        
        with open(f"{elf_file_path}_f2s.json", 'w') as out_file:
            f2s = dict()
            for CU in dwarfinfo.iter_CUs():
                line_program = dwarfinfo.line_program_for_CU(CU)
                if line_program is not None:
                    file_table = line_program['file_entry']
                    for entry in line_program.get_entries():
                        state = entry.state
                        if state is None:
                            continue
                        
                        file_name = file_table[state.file - 1].name.decode('utf-8') if state.file - 1 < len(file_table) else "N/A"
                        line_number = state.line
                        starting_address = state.address
                        starting_address_str = f'0x{starting_address:x}'
                        
                        if starting_address_str.lower() not in addr_mapping.keys():
                            continue
                        function_name = addr_mapping[starting_address_str.lower()]
                        view = 'x' if state.is_stmt else ''
                        stmt = 'x' if state.is_stmt else ''
                        if line_number > 0:
                            if function_name not in f2s.keys():
                                f2s[function_name] = {'file': str(elf_file_path), 'name': function_name, 'source': file_name, 'start': line_number, 'lines': []}
                            f2s[function_name]['lines'].append(f"{file_name}#{line_number}")
                            
            json.dump(f2s, out_file)

def name_addr_mapping(binary):
    addr_to_name = dict()
    with open(f"{binary}.json", 'r') as file:
        data = json.load(file)
    for func in tqdm(data['functions'], desc="Mapping Addresses to Func Names"):
        for block in func['blocks']:
            for src in block['src']:
                addr_to_name[src[0].lower()] = func['name']
    return addr_to_name


def main():
    parser = argparse.ArgumentParser(description="Compare binary files to identify inlined functions.")
    
    parser.add_argument("--ida", type=Path, required=True, help='Path to IDA Pro')
    parser.add_argument('--original-binary','-o', type=Path, required=True, help='Path to the original binary file from which function calls are extracted.')
    parser.add_argument('--target-binary', '-t', type=Path, required=True, help='Path to the target binary file in which inlined function calls are checked.')

    args = parser.parse_args()
    
    run_ida_script(args.ida, args.original_binary)
    addr_mapping = name_addr_mapping(args.original_binary)
    dump_debug_line(args.original_binary, addr_mapping)
    
    run_ida_script(args.ida, args.target_binary)
    addr_mapping = name_addr_mapping(args.target_binary)
    dump_debug_line(args.target_binary, addr_mapping)
    
    compare(args.original_binary, args.target_binary)

if __name__ == "__main__":
    main()

