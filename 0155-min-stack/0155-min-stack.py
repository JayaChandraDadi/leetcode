class MinStack(object):
    def __init__(self):
        self.st = []
        self.mini = None
    
    def push(self, val):
        self.st.append(val)
        if self.mini is None or val < self.mini:
            self.mini = val
        elif val >= self.mini:
            pass  # No encoding needed unless val < mini
    
    def pop(self):
        if not self.st:
            return
        x = self.st.pop()
        if not self.st:  # Stack will be empty
            self.mini = None
        elif x == self.mini:  # Recalculate minimum
            self.mini = min(self.st)
    
    def top(self):
        if not self.st:
            return None
        return self.st[-1]
    
    def getMin(self):
        if not self.st:
            return None
        return self.mini