# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bst(self,preorder,inorder,prestart,preend,instart,inend,hashmap):
        if prestart>preend or instart>inend:
            return 
        node_val = preorder[prestart]
        node = TreeNode(node_val)
        inindex = hashmap[node_val]
        numsleft = inindex-instart
        node.left = self.bst(preorder,inorder,prestart+1,prestart+numsleft,instart,inindex-1,hashmap)
        node.right = self.bst(preorder,inorder,prestart+numsleft+1,preend,inindex+1,inend,hashmap)
        return node
    def bstFromPreorder(self, preorder):
        hashmap = {}
        inorder = sorted(preorder)
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        return self.bst(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1,hashmap)