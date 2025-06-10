# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(self,postorder,poststart,postend,inorder,instart,inend,mapp):
        if poststart>postend or instart>inend:
            return None
        node = TreeNode(postorder[postend])
        inroot = mapp[node.val]
        numsleft = inroot-instart
        node.left = self.build(postorder,poststart,poststart+numsleft-1,inorder,instart,inroot-1,mapp)
        node.right = self.build(postorder,poststart+numsleft,postend-1,inorder,inroot+1,inend,mapp)
        return node
    def buildTree(self, inorder, postorder):
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        return self.build(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,mapp)

        