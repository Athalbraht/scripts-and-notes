from subprocess import check_output

print("crypto")


def decrypt(file, tmp_file='/tmp/andOTP.json'):
    try:
        check_output('gpg -d {} >> {}'.format(file, tmp_file), shell=True)
    finally:
        print('TODO exception!!')
    return tmp_file

def encrypt(file):
    pass

