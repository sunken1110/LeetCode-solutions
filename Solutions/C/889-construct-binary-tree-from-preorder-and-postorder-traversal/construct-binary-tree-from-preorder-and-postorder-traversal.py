#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description

# Complexity O(n)
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs():
            node = TreeNode(postorder.pop())

            if node.val != preorder[-1]:
                node.right = dfs()

            if node.val != preorder[-1]:
                node.left = dfs()

            preorder.pop()
            
            return node
