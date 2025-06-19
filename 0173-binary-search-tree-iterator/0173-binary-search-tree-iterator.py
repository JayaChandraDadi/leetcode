# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    stack = []
    def pushall(self,node):
        while(node!=None):
            self.stack.append(node)
            node = node.left
    def __init__(self, root):
        stack = []
        self.pushall(root)
    def next(self):
        node = self.stack.pop()
        self.pushall(node.right)
        return node.val
    def hasNext(self):
        if len(self.stack)==0:
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()