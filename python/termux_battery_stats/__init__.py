#!/usr/env python

import time
import csv
import os

from subprocess import check_output
from sys import argv

class logger():
    def __init__(self,file_name, freq=5):
        if len(argv)>1:
            self.freq = int(argv[1])
        else:
            self.freq = freq 
        self.file_name = file_name+'.csv'

        self.events = ['plug', 'screen', 'data']
        self.title = ['time','battery', 'plugin', 'wifi']
        self.termux_command = {'battery':'termux-battery-status',
                               'wifi':'termux-wifi-connectioninfo'}

        self.logs = { title:[] for title in self.title }

    def listen(self):
        try:
            b, stats = self.get_state()
            start = time.time()
            while True:
                bb, new_stats = self.get_state()
                if stats != new_stats:
                    stop = time.time()
                    _time = round((stop - start)/3600, 2)
                    b = float(b[0]) - float(bb[0])

                    data = [_time, b] + list(stats.values())
                    self.csv_update(data)
                    print('{}\n{}\n{}\n================================================='.format(stats,new_stats, data))
                    b, stats = self.get_state()

                start = time.time()
                time.sleep(self.freq)

        finally:
            print("script stopped")

    def csv_update(self, new_row):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'a') as file:
                _file = csv.writer(file)
                _file.writerow(new_row)
        else:
            with open(self.file_name, 'w') as file:
                _file = csv.writer(file)
                _file.writerow(self.title)
                _file.writerow(new_row)

    def get_info(self,_type):
        if _type == 'battery':
            _output = check_output(self.termux_command[_type])
            _output = _output.decode().split()[4:7:2]
            _output = list(map(lambda x: x[:-1], _output))
            if _output[1] == '''"UNPLUGGED"''':
                _output[1] = False
            else:
                _output[1] = True
            return _output
        elif _type == 'wifi':
            _output = check_output(self.termux_command[_type])
            _output = _output.decode().split()[2][:-1]
            if _output == 'null':
                _output = False
            else:
                _output = True
            return _output
        
        else:
            return None

    def get_state(self): 
        _states = [_type for _type in self.termux_command.keys()]
        states = [self.get_info(i) for i in _states]
        stats = {'plugin':states[0][1],
                'wifi':states[1]}
        battery=states[0][0],
        return battery, stats


if __name__ == "__main__":
    log = logger("battery_stats")
    log.listen()
