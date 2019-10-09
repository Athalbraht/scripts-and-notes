import json

def load_data(path):
        with open(path,'r') as file:
            raw = file.readlines()
            keys = {}
            for line in raw:
                tmp = line.split('|')
                keys[tmp[0]]=tmp[1]
        return keys

def write_data(keys, path):
    with open(path,'w') as file:
        for account in keys:
            file.write('{}|{}\n'.format(account,keys[account]))
    return None


def load(path):
    json_file = json.load(open(path, 'r'))
    secret_keys = {}
    for account in json_file:
        secret_keys[account['label']] = account['secret']

    return secret_keys
