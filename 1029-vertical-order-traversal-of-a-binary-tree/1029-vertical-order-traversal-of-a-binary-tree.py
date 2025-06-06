# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution(object):
    def verticalTraversal(self, root):
        ans = []
        mapp = defaultdict(lambda: defaultdict(list))
        queue = deque()
        queue.append((root,0,0))
        while(len(queue)!=0):
            node,x,y = queue.popleft()
            mapp[x][y].append(node.val)
            if node.left:
                queue.append((node.left,x-1,y+1))
            if node.right:
                queue.append((node.right,x+1,y+1))
        for x in sorted(mapp.keys()):
            vertical = []
            for y in sorted(mapp[x].keys()):
                vertical.extend(sorted(mapp[x][y]))
            ans.append(vertical)
        return ans
            
        

