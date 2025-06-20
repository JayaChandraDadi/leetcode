# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        ans = []
        def postorder(temp):
            if temp==None:
                return
            else:
                postorder(temp.left)
                postorder(temp.right)
                ans.append(temp.val)
        postorder(root)
        return ans
        