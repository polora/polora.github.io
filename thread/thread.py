import threading

class MyThread(threading.Thread):
    def __init__(self, low, high):
        super(MyThread, self).__init__()
        self.low = low
        self.high = high
        self.total = 0

    def run(self):
        for x in range(self.low, self.high):
            self.total += x

    def __str__(self):
        return f"Low: {self.low} | High: {self.high}"

thread_one = MyThread(0, 500000)
thread_two = MyThread(5000000, 10000000)
thread_one.start()
thread_two.start()
thread_one.join()
thread_two.join()
result = thread_one.total + thread_two.total
print("Result:", result)
