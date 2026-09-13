class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value =value
        self.next = None
        self.prev = None
class LRUCache:
    def insertfront(self,node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node
    def deletefromend(self,node):
        before = node.prev
        front = node.next
        before.next = front
        front.prev = before
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            node = self.hashmap[key]
            self.deletefromend(node)
            self.insertfront(node)
            return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.deletefromend(node)
            self.insertfront(node)
            return 
        node = ListNode(key,value)
        if len(self.hashmap)<self.capacity:
            self.hashmap[key] = node
            self.insertfront(node)
            return 
        else:
            endnode = self.tail.prev
            self.deletefromend(endnode)
            del self.hashmap[endnode.key]
            self.hashmap[key] = node
            self.insertfront(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)