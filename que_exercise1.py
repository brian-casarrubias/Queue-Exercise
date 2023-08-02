import threading, time, datetime
from collections import deque



class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def peek(self):
        return self.buffer[-1]
    
    
q = Queue()

orders = ['pizza','salmon', 'hotdog', 'shrimp', 'lobster', 'tamales', 'protein shake']

def placeOrder(orders):
    for order in orders:
        q.enqueue(order)
        current_time = datetime.datetime.now()
        print(f'| Time | {current_time}:| \t -------> {order.upper()} placed!')
        time.sleep(0.5)


def serveOrder():
    is_running = True

    while is_running:
        if q.is_empty():
            print('Finished Serving Everyone!!')
            break
        time.sleep(2)
        finished_order = q.dequeue()
        print(f'{finished_order} served!'.center(40, '-'))
        
    
    

print('Welcome To Casarrubias Restaurant!'.center(50, '-'))
print()


t1 = threading.Thread(target=placeOrder)
t2 = threading.Thread(target=serveOrder)

t1.start()
start_time = time.time()
time.sleep(1)
t2.start()
end_time = time.time() - start_time

print(f'Total time it took for t2 to start after t1 started:\t{end_time}s')

t1.join()
t2.join()