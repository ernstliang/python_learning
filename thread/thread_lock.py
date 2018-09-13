# 线程锁
# 有锁和无锁的区别

import threading

count_with_lock = 0
count_with_no_lock = 0
COUNT = 10000000
mlock = threading.Lock()

# 有锁的情况
def increment_with_lock():
    global count_with_lock
    for i in range(COUNT):
        mlock.acquire()
        count_with_lock += 1
        mlock.release()

def decrement_with_lock():
    global count_with_lock
    for i in range(COUNT):
        mlock.acquire()
        count_with_lock -= 1
        mlock.release()

# 无锁的情况
def increment_without_lock():
    global count_with_no_lock
    for i in range(COUNT):
        count_with_no_lock += 1

def decrement_without_lock():
    global count_with_no_lock
    for i in range(COUNT):
        count_with_no_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('count_with_lock: %s' % count_with_lock)
    print('count_with_no_lock: %s' % count_with_no_lock)
