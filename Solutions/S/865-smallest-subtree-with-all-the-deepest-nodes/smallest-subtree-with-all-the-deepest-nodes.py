#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

# Time Complexity O(N), Space Complexity O(H) where H is the height of the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(tree, depth):
            if not tree:
                return (None, depth)

            l_tree, l_depth = dfs(tree.left, depth+1)
            r_tree, r_depth = dfs(tree.right, depth+1)

            if l_depth > r_depth:
                return (l_tree, l_depth)

            elif l_depth < r_depth:
                return (r_tree, r_depth)

            else:
                return (tree, l_depth)


        return dfs(root, 0)[0]
