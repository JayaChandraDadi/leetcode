# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    stacknext = []
    stackbefore = []
    def next(self):
        node = self.stacknext.pop()
        self.pushleft(node.right)
        return node.val
    def before(self):
        node = self.stackbefore.pop()
        self.pushright(node.left)
        return node.val
    def pushleft(self,node):
        while(node!=None):
            self.stacknext.append(node)
            node = node.left
    def pushright(self,node):
        while(node!=None):
            self.stackbefore.append(node)
            node = node.right
    def findTarget(self, root, k):
        self.pushleft(root)
        self.pushright(root)
        nextel = self.next()
        beforeel = self.before()
        while(nextel<beforeel):
            if nextel+beforeel==k:
                return True
            elif nextel+beforeel<k:
                if not self.stacknext:
                    break
                nextel = self.next()
            else:
                if not self.stackbefore:
                    break
                beforeel = self.before()
        return False




        
        