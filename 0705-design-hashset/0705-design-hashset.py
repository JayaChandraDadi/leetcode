class Listnode:
    def __init__(self,value):
        self.val = value
        self.next = None
class MyHashSet:
    def __init__(self):
        self.buckets = [None]*1000
        self.size = 1000
    def add(self, key: int) -> None:
        hash_val = key % self.size
        newnode = Listnode(key)
        curr = self.buckets[hash_val]
        while(curr):
            if curr.val==key:
                return
            curr = curr.next
        newnode.next = self.buckets[hash_val]
        self.buckets[hash_val] = newnode
    def remove(self, key: int) -> None:
        hash_val = key%self.size
        curr = self.buckets[hash_val]
        if not curr:
            return
        if curr.val==key:
            self.buckets[hash_val] = curr.next
            return
        prev = None
        while(curr and curr.val!=key):
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        return 
    def contains(self, key: int) -> bool:
        hash_val = key%self.size
        curr = self.buckets[hash_val]
        while(curr):
            if curr.val==key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)