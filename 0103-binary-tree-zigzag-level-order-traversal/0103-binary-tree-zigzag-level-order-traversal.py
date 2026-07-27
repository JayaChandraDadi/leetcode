# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = 0
        q = deque()
        if not root:
            return []
        q.append(root)
        ans = []
        while(q):
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag==0:
                ans.append(temp)
                flag = 1
            else:
                ans.append(temp[::-1])
                flag = 0
        return ans