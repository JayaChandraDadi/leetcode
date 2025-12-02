# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        q = deque()
        result = ''
        q.append(root)
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    result+='#'+','
                    continue
                else:
                    result+=str(node.val)+','
                q.append(node.left)
                q.append(node.right)
        return result
    def deserialize(self, data):

        if not data:
            return None
        nodes = data.split(',')
        q = deque()
        if nodes[0]=='#':
            return None
        root = TreeNode(int(nodes[0]))
        q.append(root)
        i = 1
        while q and i<len(nodes)-1:
            node = q.popleft()
            if nodes[i]!='#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i+=1
            if nodes[i]!='#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i+=1
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))