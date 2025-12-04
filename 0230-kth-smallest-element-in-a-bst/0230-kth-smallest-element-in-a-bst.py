# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,root,ans):
        if not root:
            return
        self.preorder(root.left,ans)
        ans.append(root.val)
        self.preorder(root.right,ans)
        return ans
    def kthSmallest(self, root, k):
        ans = self.preorder(root,[])
        return ans[k-1]
        