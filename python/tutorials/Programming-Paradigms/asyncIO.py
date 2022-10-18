import asyncio
from time import sleep


async def first(a):
    print(f'-> func first({a}): start')
    task = asyncio.create_task(second(1,5))
    #sleep(2)
    #await asyncio.sleep(3)
    print(f'-> func first({a}): stop')
    ret = await task
    print(ret)


async def second(a,t):
    print(f'-> func second({a}): start')
    await asyncio.sleep(int(t))
    print(f'-> func second({a},{t}): stop')
    return 'return of second()'

async def gather(): # -> AsyncIterable[str]
    f, s = await asyncio.gather(first(2), second(2,5))



async def asa(a):
    print('as F')
    await asyncio.sleep(2)
    print('as F stop')

def as2(a):
    print('as F2')
    sleep(2)
    print('as F2 stop')

async def block():
    print('-----------')
    aaa = asyncio.create_task(asa(1))
    await asyncio.to_thread(as2,1)
    await aaa 

if __name__ == '__main__':
    #asyncio.run(first(1))
    #asyncio.run(gather())
    asyncio.run(block())
