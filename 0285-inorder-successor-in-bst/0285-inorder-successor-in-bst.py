# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,p):
        if not root:
            return 
        self.inorder(root.left,p)
        self.ans.append(root)
        self.inorder(root.right,p)
    def inorderSuccessor(self, root, p):
        self.ans = []
        self.inorder(root,p)
        n = len(self.ans)
        for i in range(len(self.ans)):
            if self.ans[i]==p:
                if i+1!=n:
                    return self.ans[i+1]
                else:
                    return None
        