# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,preorder,inorder,instart,inend,prestart,preend,hashmap):
        if instart>inend or prestart>preend:
            return 
        node = TreeNode(preorder[prestart])
        inindex = hashmap[node.val]
        numsleft = inindex-instart
        node.left = self.build(preorder,inorder,instart,inindex-1,prestart+1,prestart+numsleft,hashmap)
        node.right = self.build(preorder,inorder,inindex+1,inend,prestart+numsleft+1,preend,hashmap)
        return node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        return self.build(preorder,inorder,0,len(inorder)-1,0,len(inorder)-1,hashmap)