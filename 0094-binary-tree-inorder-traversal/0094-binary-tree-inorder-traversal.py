# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        inorder = []
        curr = root
        while(curr!=None):
            if curr.left==None: 
                inorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while(prev.right and prev.right!=curr):
                    prev = prev.right
                if prev.right==None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder
      



               
        