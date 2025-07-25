# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        if not root:
            return '[]'
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        while result and result[-1] == 'null':
            result.pop()
        
        return '[' + ','.join(result) + ']'
    def deserialize(self, data):
        if data == '[]':
            return None
        nodes = data[1:-1].split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i < len(nodes) and nodes[i] != 'null':
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] != 'null':
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))