from tqdm import tqdm
import json
import pandas as pd


def compare(query_file, repository_file):

    dataset = {
        'caller': [],
        'callee': [],
        'label': []
    }

    with open(f"{query_file}.json", 'r') as file:
        query_functions = json.load(file)

    with open(f"{query_file}_f2s.json", 'r') as file:
        query_f2s = json.load(file)

    with open(f"{repository_file}_f2s.json", 'r') as file:
        repository = json.load(file)

    call_dict = dict()
    for func in tqdm(query_functions['functions'], desc="Getting Function Calls"):
        for blocks in func['blocks']:
            for src in blocks['src']:
                if src[1] == 'call':
                    if func['name'] not in call_dict.keys():
                        call_dict[func['name']] = set()
                    call_dict[func['name']].add(src[2])
                    
        if func['name'] not in call_dict.keys(): # No function call
            call_dict[func['name']] = set()
                    
                        
    for func in tqdm(query_functions['functions'], desc="Searching for Inlined Calls"):
        if func['name'] not in query_f2s.keys() or func['name'] not in repository.keys(): # Skipping compiler or eliminated functions
            continue
        
        
        calls = list(call_dict[func['name']])
        already_added_calls = set()

        while calls:
            call = calls.pop(0)
            already_added_calls.add(call)
            label = 0
            if call not in query_f2s.keys(): # Compiler callee functions
                dataset['caller'].append(func['name'])
                dataset['callee'].append(call)
                dataset['label'].append(label)
            else:
                q_set = set(query_f2s[call]['lines'])
                repo_set = set(repository[func['name']]['lines'])
                for line in q_set:
                    if line in repo_set:
                        label = 1
                        if call in call_dict.keys():
                            inner_calls = call_dict[call]
                            calls.extend([_call for _call in inner_calls if _call not in already_added_calls])
                        break
                dataset['caller'].append(func['name'])
                dataset['callee'].append(call)
                dataset['label'].append(label)

    dataset = pd.DataFrame(dataset)
    print("Saving result...")
    dataset.to_csv(f'{query_file}.csv', index=False)


