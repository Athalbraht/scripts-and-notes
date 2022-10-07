#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from sys import argv

def f(R,_R,T,o):
    return (T-_R+2*R)/(2*o) - R

def get_time(R,_R,T,o):
    w = f(R,_R,T,o)
    pr = 2*o*w/T
    ln = (o*w+(o-1)*R)
    print(ln)
    plt.plot(R*60,w*60,'ro-',label='work vs break [min]')
    plt.plot(R*60,100*pr,'g--', label='percent of work')
    plt.plot(R*60,pr*8*10,'y--', label='real time of working [h*10]')
    plt.title("lunch after {} h".format(ln.mean()))
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.clf()
    return None

if __name__ == "__main__":
    print("""
    args: 
    1. full working time [h]
    2. work segments before long break in half
    3. long break time [min]
    """)
    T = float(argv[1])
    o = float(argv[2])
    _R = float(argv[3])
    R = np.linspace(0,_R/60,100)
    get_time(R, _R/60, T, o)

