# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allpaths(self,root,st,ans):
        if not root:
            return 
        st.append(str(root.val))
        if root.left==None and root.right==None:
            ans.append('->'.join(st))
        else:
            if root.left:
                self.allpaths(root.left,st,ans)
                st.pop()
            if root.right:
                self.allpaths(root.right,st,ans)
                st.pop()
        return ans
    def binaryTreePaths(self, root):
        if not root:
            return 
        st = []
        return self.allpaths(root,st,[])
        