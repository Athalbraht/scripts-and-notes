import time
import subprocess as sp
from random import shuffle
from datetime import datetime
from tqdm import tqdm

def load_channels(_file="channels.txt"):
    print('Loading channels list...')
    try:
        file = open(_file,'r')
        channels = file.readlines()
        #print(channels)
        channels = [float(channel) for channel in channels]
        shuffle(channels)
        file.close()
        #print(channels)
        print("Done")
    except:
        print("Failed to load {} list".format(_file))
        exit()
    finally:
        print('\n')
    return channels

def transmission(_channels, _file, _delay=0):
    errors = []
    date = datetime.now()
    print("->{} Starting transmission on {} channels".format(date.strftime("%d-%b %H:%M") ,len(_channels)))
    bar = tqdm(_channels, desc="Transmission:", ascii=True, bar_format="{l_bar}{bar}| {postfix}]")
    for channel in bar:
        bar.set_postfix(freq="{}MHz".format(channel))
        # print(channel)
        try:
            output = sp.check_output('sox -t mp3 {} -t wav - |sudo ~/PiFmRds/src/pi_fm_rds -freq {}  -rt "Japan Music" -audio - 2>/dev/null'.format(_file, channel),shell=True)
        #except:
         #   errors.append(channel)
        finally:
            time.sleep(_delay)
    print("--->Transmission done. Errors occured {} times.".format(len(errors)))
    if len(errors)>0:
        print("-->Errors on channels: {}".format(errors))
        errors = []

if __name__ == '__main__':
    
    night = False
    day = True
    channels = load_channels()


    print("Testing on 104.4MHz and 88.9MHz...\n")
    transmission([104.4,88.9],"testous.mp3")
    print("\nContinue? [Y/n]")
    _char = input()
    if _char == "n" or _char=="N":
        exit()

    while True:
        clock = datetime.now()
        if clock.time().hour==20 and clock.time().minute>25 and night==False:
            print("\n-----{} Starting NIGHT:--------".format(clock.strftime("%d-%b %H:%M")))
            night = True
            day = False
            for i in range(1):
                transmission([103.7], "testoshort.mp3")
                time.sleep(60*7)
            transmission([103.7], "szum2.mp3")

        clock = datetime.now()
        if clock.time().hour>9 and clock.time().hour<18 and day==False:
            print("\n-----{} Starting DAY:--------".format(clock.strftime("%d-%b %H:%M")))
            day = True
            night = False
            for i in range(2):
                transmission(channels, "4sec.mp3")
                time.sleep(10*60)
        time.sleep(7*60)
        print("checked at {}".format(clock.strftime("%d-%b %H:%M")))

