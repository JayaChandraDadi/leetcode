# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        queue = deque()
        mapp = {}
        queue.append(root)
        while(len(queue)!=0):
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    mapp[node.left] = node
                    queue.append(node.left)
                if node.right:
                    mapp[node.right] = node
                    queue.append(node.right)
        vis = {}
        dis = 0
        vis[target] = True
        queue.append(target)
        while(len(queue)!=0):
            length = len(queue)
            if dis==k:
                break
            for i in range(length):
                node = queue.popleft()
                if node.left and not vis.get(node.left, False):
                    vis[node.left] = True
                    queue.append(node.left)
                if node.right and not vis.get(node.right, False):
                    vis[node.right] = True
                    queue.append(node.right)
                if node in mapp and not vis.get(mapp[node], False):
                    vis[mapp[node]] = True
                    queue.append(mapp[node])
            dis+=1
        ans = []
        while(len(queue)!=0):
            node = queue.popleft()
            ans.append(node.val)
        return ans
                
                
            




        