# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(self,preorder,prestart,preend,inorder,instart,inend,mapp):
        if prestart>preend or instart>inend:
            return None
        node = TreeNode(preorder[prestart])
        numsleft = mapp[node.val]-instart
        inroot = mapp[node.val]
        node.left = self.build(preorder,prestart+1,prestart+numsleft,inorder,instart,inroot-1,mapp)
        node.right = self.build(preorder,prestart+1+numsleft,preend,inorder,inroot+1,inend,mapp)
        return node
    def buildTree(self, preorder, inorder):
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        return self.build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,mapp)
        