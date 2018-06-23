import asyncio
import threading
import time
import logging

logging.basicConfig(
    # filename='async_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s:%(funcName)15s:%(lineno)5s%(levelname)8s:%(name)10s:%(message)s',
    datefmt='%Y/%m/%d %I:%M:%S'
)

logger = logging.getLogger('async_log')

async def myWorkerLock(lock):
    logger.debug("Attempting to attain lock")
    # acquire lock
    with await lock:
        # run critical section of code
        logger.debug("Currently Locked")
        # 使用time.sleep 会阻塞整个协程调度，
        # 获取lock后，协程睡3s, time.sleep无法切换到其他协程.
        # await asyncio.sleep 可以切换到信号量获取协程.
        # 释放锁后，请求lock的协程获取锁成功.
        # time.sleep(3)
        await asyncio.sleep(3)
    # our worker releases lock at this poit
    logger.debug("Unlocked Critical Section")

async def myWorkerSem(semaphore):
    await semaphore.acquire()
    logger.debug("Successfully acquired the semaphore id:{}".format(threading.get_ident()))
    await asyncio.sleep(3)
    logger.debug("Releasing Semaphore")
    semaphore.release()

async def main(loop):
    mySemaphore = asyncio.Semaphore(value=2)
    myLock = asyncio.Lock()
    future = [
        myWorkerLock(myLock), myWorkerLock(myLock), 
        myWorkerSem(mySemaphore), myWorkerSem(mySemaphore)
    ]
    logger.debug(future)
    await asyncio.wait(future)
    logger.debug("Main Coroutine end")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    except Exception as ext:
        logger.debug(ext)
    finally:
        loop.close()
    
