# Mac changer script from
# https://github.com/aszadzinski/scripts-notes-etc.git

import pdb
import logging
from sys import argv
from time import time, sleep
from random import Random
from optparse import OptionParser
from subprocess import check_output 

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

def commands(mac, interface):
    _commands = {
            "idown":"ifconfig {} down ".format(interface),
            "setmac":"ifconfig {} hw ether {}".format(interface, mac),
            "iup":"ifconfig {} up".format(interface)
            }
    return _commands

def gen_mac():
    rand = Random()
    rand.seed(time())
    mac = []
    for i in range(6):
        mac.append(hex(rand.randint(1,255))[2:])
    mac = ":".join(mac)
    return mac

def check_mac(mac):
    m_a_c = mac.split(":")
    if len(m_a_c) != 6:
        return False
    else:
        mac_int = list(map(lambda x: int(x, 16), m_a_c))
        for i in mac_int:
            if i>255:
                return False
        return True


def main():
    opt = OptionParser()
    opt.add_option('-r', '--random', help="set random MAC", dest="random", action="store_true", default=False)
    opt.add_option('-m', '--mac', help="set new mac", dest="MAC", default="ddd")
    opt.add_option('-i', '--interface', help="set interface", dest="interface", default="wlp2s0")
    opt.add_option('-v', '--verbose', help="set verbose mode", dest="debug", action="store_true", default=False)
    
    o, _ = opt.parse_args()
    
    if o.debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.ERROR)

    log.debug("PARAMS: {} {} {}".format(o.random, o.MAC, o.interface))
    log.info("Changing MAC...")
    if o.random:
        log.debug("start gen MAC")
        mac = gen_mac()
        log.debug("generated MAC: {}".format(mac))
    else:
        log.debug("setting MAC {}".format(o.MAC))
        if check_mac(o.MAC):
            log.debug("check_mac->PASS")
            mac = o.MAC
        else:
            log.error("Wrong MAC adress")
            exit()
    try:
        #pdb.set_trace()
        log.debug("Try: change MAC")
        comm = commands(mac, o.interface)
        for desc,command in comm.items():
            log.debug("executing {} command: {}".format(desc, command))
            check_output(command,shell=True)
            sleep(1)
        print("MAC changed to {} for {} interface".format(mac, o.interface))
    except Exception as e:
        log.error(e)
    





if __name__ == "__main__":
   main() 
