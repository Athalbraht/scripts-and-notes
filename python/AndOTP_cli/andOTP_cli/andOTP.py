
import getopt
from sys import argv
import logging
from . import view
from . import crypto
from . import fadb


class andOTP:
    def __init__(self):
        self.tmp_file = '/tmp/andOTP.json'
        self.path = ''
        self.alg = '--base32'
        self.method = '-totp'
        self.iterations = '6'

        self.temp_path = '/tmp/andOTP'


    def decoder(self, key):
        return 'oathtool {} {} {} -d {}'.format(self.alg, self.method, key, self.iterations)

    def load(self, path):
        if '.gpg' in path:
            pass
        elif 'json' in path:
            keys = fadb.load(path)
            #print(keys)
            print("Loaded json file from {}".format(path))
            fadb.write_data(keys, self.temp_path)
            print("Temporary saved in {}".format(self.temp_path))

    def show(self):
        temp = fadb.load_data(self.temp_path)
        print(temp)
    '''
    def run(self):
        for keys in secret_keys:
            print(keys+'---> '+subprocess.check_output(self.decoder(secret_keys[keys]),shell=True).decode())
        return None
'''
def main():
    opts, args = getopt.getopt(argv[1:], "i:e:hpas", ["import=", "export=", "help", "pgp", "aes", "show"])

    session = andOTP()

    for o, a in opts:
        if o=='-i' or o=='--import':
            session.load(a)
        elif o=='-s' or o=='--show':
            session.show()


    #print(opts)
