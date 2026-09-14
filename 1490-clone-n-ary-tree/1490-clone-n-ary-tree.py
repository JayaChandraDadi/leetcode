"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import deque
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return
        hashmap = {}
        new_node = Node(root.val)
        q = deque()
        q.append(root)
        hashmap[root] = new_node
        while(q):
            node = q.popleft()
            for nei in node.children:
                new_nei = Node(nei.val)
                hashmap[node].children.append(new_nei)
                hashmap[nei] = new_nei
                q.append(nei)
        return new_node