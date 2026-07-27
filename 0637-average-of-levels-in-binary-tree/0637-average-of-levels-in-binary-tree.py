# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        ans = []
        while(q):
            n = len(q)
            ct = 0
            sum1 = 0
            for i in range(n):
                node = q.popleft()
                sum1+=node.val
                ct+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum1/ct)
        return ans