# 使用条件进行线程同步
# 生产者-消费者模式

from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print('Consumer notify: no item to consume')
        items.pop()
        print("Consumer notify: consumed 1 item")
        print("Consumer notify: items to consumer are %d" % len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(2)
            self.consume()

class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print('Producer notify: items producted are %d' % len(items))
            print('Producer notify: stop the production!!!')
        items.append(1)
        print("Producer notify: total items producted %d" % len(items))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(0.5)
            self.produce()

if __name__ == '__main__':
    producer = producer()
    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()