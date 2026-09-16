# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        parent_child_map = {}
        for parent,child,isleft in descriptions:
            if parent not in hashmap:
                parent_node = TreeNode(parent)
                hashmap[parent] = parent_node
            if child not in hashmap:
                child_node = TreeNode(child)
                hashmap[child] = child_node
            if isleft==1:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]
            parent_child_map[child] = parent
            if parent not in parent_child_map:
                parent_child_map[parent] = -1
        for parent,child in parent_child_map.items():
            if child==-1:
                return hashmap[parent]