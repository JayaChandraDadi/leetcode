# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
       self.nums = []
       self.inorder(root)
       self.index = 0
       self.n = len(self.nums)
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)
    def next(self):
        if self.index<self.n:
            temp = self.index
            self.index+=1
            return self.nums[temp]
    def hasNext(self):
        if self.index+1<=self.n:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()