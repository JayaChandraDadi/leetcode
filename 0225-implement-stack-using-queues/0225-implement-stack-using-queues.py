from Queue import Queue

class MyStack(object):

    def __init__(self):
        self.q = Queue()

    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())

    def pop(self):
        return self.q.get()
    def top(self):
        return self.q.queue[0]

    def empty(self):
        if self.q.qsize()==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()