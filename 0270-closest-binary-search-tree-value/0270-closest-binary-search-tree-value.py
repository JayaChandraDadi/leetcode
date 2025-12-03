# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    ans = 0
    def search(self,root,target,value):
        if not root:
            return 
        difference = abs(target-root.val)
        if difference>value:
            return 
        else:
            value = difference
            self.ans = root.val
            if target>root.val:
                self.search(root.left,target,value)
            else:
                self.search(root.right,target,value)
    def closestValue(self, root, target):
        q = deque()
        q.append(root)
        difference = float('inf')
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if difference>abs(node.val-target):
                    difference = abs(node.val-target)
                    ans = node.val
                if difference==abs(node.val-target):
                    if node.val-target<ans-target:
                        ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

        self.search(root,target,float('inf'))
        return self.ans
        