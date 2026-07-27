# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flat(self,root):
        if not root:
            return 
        if root.left==None:
            self.flat(root.right)
        else:
            temp = root.right
            root.right = root.left
            temp1 = root
            root.left = None
            while(temp1.right!=None):
                temp1 = temp1.right
            temp1.right = temp
            self.flat(root.right)
        return root
    def flatten(self, root: Optional[TreeNode]) -> None:
        return self.flat(root)
        return root