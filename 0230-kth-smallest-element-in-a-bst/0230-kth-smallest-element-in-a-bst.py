# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        node = root
        ct = 0
        while(node):
            if node.left==None:
                ct+=1
                if ct==k:
                    return node.val
                node = node.right
            else:
                prev = node.left
                while prev.right!=node and prev.right!=None:
                    prev = prev.right
                if prev.right==None:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    ct+=1
                    if ct==k:
                        return node.val
                    node = node.right
        return None

        
        