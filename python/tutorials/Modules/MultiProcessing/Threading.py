from threading import Thread
import time 

def f(a,b):
    time.sleep(4.5)
    print(f'-> {a} {b}')

###### opt #############################
#barrier = threading.Barrier(2) #numof threads
#barrier.wait()
#lock = threading.Lock()
#lock.aquire()
#lock.release()
############################################




x = Thread(target=f, args=(3,5))
x.run()
