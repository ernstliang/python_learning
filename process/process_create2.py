import multiprocessing
import process_create

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=process_create.foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()