# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree(self,preorder,inorder,prestart,preend,instart,inend,hashmap):
        if prestart>preend or instart>inend:
            return 
        root_val = preorder[prestart]
        root = TreeNode(root_val)
        inindex = hashmap[root_val]
        numsleft = inindex-instart
        root.left = self.tree(preorder,inorder,prestart+1,prestart+numsleft,instart,inindex-1,hashmap)
        root.right = self.tree(preorder,inorder,prestart+numsleft+1,preend,inindex+1,inend,hashmap)
        return root
    def buildTree(self, preorder, inorder):
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        return self.tree(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1,hashmap)
    