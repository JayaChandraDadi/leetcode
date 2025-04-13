from Queue import LifoQueue
class MyQueue(object):

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()
    def push(self, x):
        self.s1.put(x)
    def pop(self):
        if self.s2.qsize()==0:
            while(self.s1.qsize()!=0):
                self.s2.put(self.s1.get())
        return self.s2.get()
    def peek(self):
        if self.s2.qsize()==0:
            while(self.s1.qsize()!=0):
                self.s2.put(self.s1.get())
        return self.s2.queue[-1]
        

    def empty(self):
        if self.s1.qsize()==0 and self.s2.qsize()==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()