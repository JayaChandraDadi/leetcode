# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bst(self,nums,left,right):
        if left>right:
            return 
        mid = (left+right)//2
        root = TreeNode(nums[mid])
        root.left = self.bst(nums,left,mid-1)
        root.right = self.bst(nums,mid+1,right)
        return root
    def sortedArrayToBST(self, nums):
        return self.bst(nums,0,len(nums)-1)