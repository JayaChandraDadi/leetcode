# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Bstiterator(object):
    def __init__(self,root,isreverse):
        self.st = []
        self.reverse = isreverse
        self.pushall(root,self.reverse)
    def pushall(self,root,reverse):
        while(root):
            self.st.append(root)
            if reverse:
                root = root.right
            else:
                root = root.left
    def next(self):
        node = self.st.pop()
        if not self.reverse:
            self.pushall(node.right,self.reverse)
        else:
            self.pushall(node.left,self.reverse)
        return node.val
class Solution(object):
    def findTarget(self, root, k):
        l = Bstiterator(root,False)
        r = Bstiterator(root,True)
        i = l.next()
        j = r.next()
        while(i<j):
            sum1 = i+j
            if sum1>k:
                j = r.next()
            elif sum1<k:
                i = l.next()
            else:
                return True
        return False

        