# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
       self.st = []
       self.inorder_left(root)
    def inorder_left(self,root):
        while(root):
            self.st.append(root)
            root = root.left
    def next(self):
        node = self.st.pop()
        if node.right:
            self.inorder_left(node.right)
        return node.val
    def hasNext(self):
        if len(self.st)!=0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()