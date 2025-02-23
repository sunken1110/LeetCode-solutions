#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description

# Complexity O(n)
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        preorder = re.findall('(-*)(\d+)', traversal)
        nodes = [(len(node[0]), int(node[1])) for node in preorder][::-1]

        def dfs(level):
            if not nodes or level != nodes[-1][0]:
                return

            node = TreeNode(nodes.pop()[1])
            node.left = dfs(level + 1)
            node.right = dfs(level + 1)

            return node

        return dfs(0)
