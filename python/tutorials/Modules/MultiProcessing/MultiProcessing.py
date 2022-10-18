import multiprocessing as mp
import time 

def test(x):
    print('test {}'.format(x))

def f(x):
    return x**2
'''
time.sleep(4)
for i in range(33):
    a = mp.Process(target=test,args=(i,))
    a.start()
    a.join()
'''
#p = mp.Pool(processes=4)
#tab = p.map(f, range(10))
#p.close()
#print(tab)




##########################################

def do_stuff(x=10000000):
    a = [ float(i) for i in range(x)]
    for i in range(1,len(a)):
        a[i] /= a[i]+4
    return a

def f(cpu,l=[41235,412512,1541224]):
    st = time.time()
    with mp.Pool(processes=cpu) as p:
        r = p.map(do_stuff,l)
    print(f'{(time.time()-st)} s')

if __name__ == '__main__':
    with mp.Pool(processes=2) as p:
        #res = p.imap_unordered(test,list(range(20))) #do only few items from list then quit
        res = p.map(test,list(range(20)))
        #res = p.imap(test,list(range(20)))
    f(1)
