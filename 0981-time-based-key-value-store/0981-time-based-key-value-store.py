class TimeMap:

    def __init__(self):
        self.hashmap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ''
        arr = self.hashmap[key]
        low = 0
        high = len(arr) - 1
        ans = ''
        while(low<=high):
            mid = (low + high)//2
            time,value = arr[mid]
            if time<=timestamp:
                ans = value
                low = mid + 1
            else:
                high = mid - 1
        return ans
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)