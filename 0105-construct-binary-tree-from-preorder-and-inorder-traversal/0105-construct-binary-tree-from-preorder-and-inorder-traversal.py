# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,prestart,preend,instart,inend,preorder,inorder,hashmap):
        if prestart>preend or instart>inend:
            return None
        val = preorder[prestart]
        inindex = hashmap[val]
        node = TreeNode(val)
        numsleft = inindex - instart
        node.left = self.dfs(prestart+1,prestart+numsleft,instart,inindex-1,preorder,inorder,hashmap)
        node.right = self.dfs(prestart+numsleft+1,preend,inindex+1,inend,preorder,inorder,hashmap)
        return node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        n = len(preorder)
        for i in range(n):
            hashmap[inorder[i]] = i
        return self.dfs(0,n-1,0,n-1,preorder,inorder,hashmap)