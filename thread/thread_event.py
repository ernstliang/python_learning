# 事件同步机制
# 生产者-消费者模式

from threading import Thread, Event
import time
import random

m_exit = False
items = []
event = Event()

class consumer(Thread):
    def __init__(self, event):
        self.event = event
        Thread.__init__(self)

    def consume(self):
        global items
        time.sleep(0.1)
        self.event.wait()
        i = items.pop()
        print("Consumer notify: consumed 1 item %d" % i)
        print("Consumer notify: items to consumer are %d" % len(items))
        
    def run(self):
        while not m_exit:
            self.consume()

class producer(Thread):
    def __init__(self, event):
        self.event = event
        Thread.__init__(self)

    def produce(self):
        global items
        items.append(1)
        print("Producer notify: total items producted %d" % len(items))
        self.event.set()
        print('Producer notify: set items producted %d' % len(items))
        self.event.clear()
        
    def run(self):
        global m_exit
        for i in range(0, 20):
            time.sleep(0.5)
            self.produce()
        m_exit = True

if __name__ == '__main__':
    producer = producer(event)
    consumer = consumer(event)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()