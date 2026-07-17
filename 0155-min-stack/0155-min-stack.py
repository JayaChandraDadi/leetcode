class MinStack:

    def __init__(self):
        self.st = []
    def push(self, value: int) -> None:
        if not self.st:
            self.st.append([value,value])
            return
        current_min1 = self.st[-1][1]
        updated_min1 = min(current_min1,value)
        self.st.append([value,updated_min1]) 
    def pop(self) -> None:
        if not self.st:
            return 
        self.st.pop()
    def top(self) -> int:
        if not self.st:
            return 
        return self.st[-1][0]

    def getMin(self) -> int:
        if not self.st:
            return
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()