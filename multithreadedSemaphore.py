#Simple multithreaded processing with semaphor in python (Just an example, not optimized)
import time
import threading
from threading import Thread

#replace myfunc with your own function****
def myfunc(i,pool_sema):
    with pool_sema:
        print("Sleeping 5 sec from thread %d \n" % i)    
        time.sleep(5)	
        print("Finished sleeping from thread %d \n" % i)
    

if __name__ == '__main__':
    maxconnections = 5 # Define number of limited resources avaialable
    pool_sema = threading.BoundedSemaphore(value=maxconnections)
    for i in range(10):    #define and start 10 threads    
        t = Thread(target=myfunc, args=(i,pool_sema)) 
        t.start()
