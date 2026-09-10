# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchbst(self,node,val):
        if (node==None):
            return None 
        if (node.val==val):
            return node
        if (val>node.val):
            return self.searchbst(node.right,val)
        return self.searchbst(node.left,val)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchbst(root,val)