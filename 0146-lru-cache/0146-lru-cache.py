class ListNode(object):

    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache(object):
    def deletenode(self,temp):
        back = temp.prev
        front = temp.next
        back.next = front
        front.prev = back
        temp.next = None
        temp.prev = None
    def insertafterhead(self,temp):
        front = self.head.next
        self.head.next = temp
        temp.next = front
        front.prev = temp
        temp.prev = self.head
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key):
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.deletenode(node)
        self.insertafterhead(node)
        return node.value
    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.deletenode(node)
            self.insertafterhead(node)
        else:
            if self.capacity==len(self.hashmap):
                node = self.tail.prev
                self.deletenode(node)
                del self.hashmap[node.key]
            newnode = ListNode(key,value)
            self.hashmap[key] = newnode
            self.insertafterhead(newnode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)