import subprocess
import argparse
from pathlib import Path
import os

def run(args):
    try:
        current_directory = os.path.abspath(os.getcwd())
        script_path = os.path.join(current_directory, "fin\\main.py")
        py_path = os.path.join(current_directory, ".venv\\Scripts\\python.exe")
        command = [f'{py_path}', f'{script_path}', "--ida", f'{args.ida}', "-o", f'{args.original_binary}', "-t", f'{args.target_binary}']
        #print(' '.join(command))
        subprocess.run(
            command,
            check=True,
            shell=True
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e.stderr}")

def main():
    parser = argparse.ArgumentParser(description="Compare binary files to identify inlined functions.")
    
    parser.add_argument("--ida", type=Path, required=True, help='Path to IDA Pro')
    parser.add_argument('--original-binary','-o', type=Path, required=True, help='Path to the original binary file from which function calls are extracted.')
    parser.add_argument('--target-binary', '-t', type=Path, required=True, help='Path to the target binary file in which inlined function calls are checked.')

    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()