# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
            temp1 = []
            temp2 = []
            def paths(node,temp,key):
                if not node:
                    return False
                temp.append(node)
                if node.val==key.val:
                    return True
                if paths(node.left,temp,key) or paths(node.right,temp,key):
                    return True
                temp.pop()
                return False
            paths(root,temp1,p)
            paths(root,temp2,q)
            i = 0
            while i < len(temp1) and i < len(temp2) and temp1[i] == temp2[i]:
                i += 1
            return temp1[i-1]
        