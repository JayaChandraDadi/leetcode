class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0
    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val]+=1
        self.maxfreq = max(self.maxfreq,self.freq[val])
        ct = self.freq[val]
        if ct not in self.group:
            self.group[ct] = []
        self.group[ct].append(val)
    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x]-=1
        if not self.group[self.maxfreq]:
            self.maxfreq-=1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()