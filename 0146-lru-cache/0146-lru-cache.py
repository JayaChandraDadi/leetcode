class Node:
    def __init__(self,key,value,next=None,prev= None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapp = {}
    def deletenode(self,node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
    def insertafterhead(self,node):
        currafterhead = self.head.next
        self.head.next = node
        currafterhead.prev = node
        node.next = currafterhead
        node.prev = self.head
    def get(self, key):
        if key not in self.mapp:
            return -1
        else:
            temp = self.mapp[key]
            self.deletenode(temp)
            self.insertafterhead(temp)
        return temp.value
    def put(self, key, value):
        if key in self.mapp:
            temp = self.mapp[key]
            temp.value = value
            self.deletenode(temp)
            self.insertafterhead(temp)
        else:
            if len(self.mapp)>=self.capacity:
                temp = self.tail.prev
                self.mapp.pop(temp.key)
                self.deletenode(temp)
            newnode = Node(key,value)
            self.mapp[key] = newnode
            self.insertafterhead(newnode)
