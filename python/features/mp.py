import multiprocessing as mp
import time 

def test(x):
    print('test {}'.format(x))

def f(x):
    return x**2

time.sleep(4)
for i in range(33):
    a = mp.Process(target=test,args=(i,))
    a.start()
    a.join()

p = mp.Pool(processes=4)
tab = p.map(f, range(10))
p.close()
print(tab)
