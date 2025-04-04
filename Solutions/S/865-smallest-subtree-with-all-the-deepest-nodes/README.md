**Smallest Subtree with all the Deepest Nodes**
=
[Problem Link](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/)

## Intuition
The following problem is an duplication of this problem: 
[Problem Link](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description)

We use postorder recursion to traver a tree. Get a depth when we reach the deepest leaves of each subtree, and then 
return the maximal depth. If the depth of left and right subtrees equal, then the current node is the lowest common 
ancestor of this subtree. If not, then recurse into more deeper subtree.

## Approach
**Step-by-Step Process**

1. Construct a DFS algorithm for a postorder recursion.

2. If the deepest leaf found, then return the current depth.

3. If any subtrees exist, then recurse into more deeper subtree.
  
## Solutions
```python
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
```
