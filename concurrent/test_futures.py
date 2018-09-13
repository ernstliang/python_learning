from concurrent import futures
import time

number_list = [x+1 for x in range(10)]

def count(num):
    for i in range(0, 10000000):
        i = i+1
    return i * num

def evaluate_item(x):
    ret = count(x)
    return ret

def run():
    # 循序执行
    start_time = time.time()
    for item in number_list:
        print(evaluate_item(item))
    print('Sequential execution in ' + str(time.time() - start_time), "seconds")

    # 线程执行
    start_time = time.time()
    with futures.ThreadPoolExecutor(max_workers = 5) as executor:
        func = [executor.submit(evaluate_item, item) for item in number_list]
        for future in futures.as_completed(func):
            print(future.result())
    print('Thread pool execution in ' + str(time.time() - start_time), "seconds")

    # 进程执行
    start_time = time.time()
    with futures.ProcessPoolExecutor(max_workers = 5) as executor:
        func = [executor.submit(evaluate_item, item) for item in number_list]
        for future in futures.as_completed(func):
            print(future.result())
    print('Process pool execution in ' + str(time.time() - start_time), "seconds")

if __name__ == '__main__':
    print(number_list)
    run()
