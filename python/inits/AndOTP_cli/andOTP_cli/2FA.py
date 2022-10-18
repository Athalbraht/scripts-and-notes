#!/usr/bin/env python3

import subprocess
import json
from sys import argv

def decrypter(file):
    subprocess.check_output('gpg -d {} >> /tmp/accountsOTP_plain.json'.format(file),shell=True)
    return None

def decoder(key):
    return 'oathtool --base32 --totp {} -d 6'.format(key)

json_file = json.load(open(str(argv[1]),'r'))
secret_keys = {}
for account in json_file:
    secret_keys[account['label']] = account['secret']

for keys in secret_keys:
    print(keys+' --> '+subprocess.check_output(decoder(secret_keys[keys]), shell=True).decode())


