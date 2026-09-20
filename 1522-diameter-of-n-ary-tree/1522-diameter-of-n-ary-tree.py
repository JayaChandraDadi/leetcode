"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        def dfs(root):
            first_max = 0
            second_max = 0
            for nei in root.children:
                height = dfs(nei)
                if height>first_max:
                    second_max = first_max
                    first_max = height
                elif height>second_max:
                    second_max = height
                self.diameter = max(self.diameter,first_max + second_max)
            return 1 + first_max
        self.diameter = 0
        dfs(root)
        return self.diameter