# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Queue import Queue
class Solution(object):
    def levelOrder(self, root):
        queue = Queue()
        ans = []
        if root == None:
            return ans
        queue.put(root)
        while(queue.qsize()!=0):
            n = queue.qsize()
            k = []
            for i in range(n):
                temp = queue.get()
                if temp.left!=None:
                    queue.put(temp.left)
                if temp.right!=None:
                    queue.put(temp.right)
                k.append(temp.val)
            ans.append(k)
        return ans
                

        
        
       
        