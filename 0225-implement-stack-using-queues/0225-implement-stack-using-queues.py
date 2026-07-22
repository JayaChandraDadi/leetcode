from collections import deque
class MyStack:

    def __init__(self):
       self.q1 = deque()
       self.q2 = deque() 
       self.top_el = 0
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_el = x
    def pop(self) -> int:
        while(len(self.q1)>1):
            self.top_el = self.q1.popleft()
            self.q2.append(self.top_el)
        popped_el = self.q1.popleft()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return popped_el
    def top(self) -> int:
        return self.top_el
    def empty(self) -> bool:
        return len(self.q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()