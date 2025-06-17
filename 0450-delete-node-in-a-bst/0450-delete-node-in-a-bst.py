# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self,node):
        if node.left==None:
            return node.right
        elif node.right==None:
            return node.left
        rightnode = node.right
        lastright = node.left
        while(lastright.right!=None):
            lastright = lastright.right
        lastright.right = rightnode
        return node.left
    def deleteNode(self, root, key):
        if not root:
            return
        if root.val == key:
            return self.helper(root)
        node = root
        while(node):
            if key<node.val:
                if node.left!=None and node.left.val==key:
                    node.left = self.helper(node.left)
                    break
                else:
                    node = node.left
            elif key>node.val:
                if node.right!=None and node.right.val==key:
                    node.right = self.helper(node.right)
                    break
                else:
                    node = node.right
        return root
        
        