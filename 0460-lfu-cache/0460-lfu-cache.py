class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # dummy head
        self.tail = Node(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        prevn = node.prev
        nextn = node.next
        prevn.next = nextn
        nextn.prev = prevn
        self.size -= 1

    def pop_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_dll = {}
        self.min_freq = 0

    def _update_freq(self, node):
        freq = node.freq
        self.freq_to_dll[freq].remove_node(node)
        if self.freq_to_dll[freq].size == 0:
            if freq == self.min_freq:
                self.min_freq += 1
            del self.freq_to_dll[freq]

        node.freq += 1
        freq = node.freq
        if freq not in self.freq_to_dll:
            self.freq_to_dll[freq] = DoublyLinkedList()
        self.freq_to_dll[freq].insert_at_head(node)

    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                # Evict least frequent, least recently used
                dll = self.freq_to_dll[self.min_freq]
                node_to_evict = dll.pop_tail()
                del self.key_to_node[node_to_evict.key]

            # Insert new node
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].insert_at_head(new_node)
            self.min_freq = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)