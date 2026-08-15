"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self,node,visited):
        if not node:
            return 
        if node in visited:
            return visited[node]
        clone_node = Node(node.val)
        visited[node] = clone_node
        for nei in node.neighbors:
            clone_node.neighbors.append(self.dfs(nei,visited))
        return clone_node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        return self.dfs(node,visited)