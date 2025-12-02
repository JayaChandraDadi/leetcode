# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree(self,postorder,inorder,poststart,postend,instart,inend,hashmap):
        if poststart>postend or instart>inend:
            return 
        root_val = postorder[postend]
        root = TreeNode(root_val)
        rootindex = hashmap[root_val]
        numsleft = rootindex-instart
        root.left = self.tree(postorder,inorder,poststart,poststart+numsleft-1,instart,rootindex-1,hashmap)
        root.right = self.tree(postorder,inorder,poststart+numsleft,postend-1,rootindex+1,inend,hashmap)
        return root
    def buildTree(self, inorder, postorder):
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        return self.tree(postorder,inorder,0,len(postorder)-1,0,len(inorder)-1,hashmap)