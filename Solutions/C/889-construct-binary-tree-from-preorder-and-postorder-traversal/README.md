**Construct Binary Tree From Preorder and Postorder Traversal**
=
[Problem Link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description)

## Intuition
Consider a tree with depth only 2, that is, one parent node and two child nodes. 
Then the preorder is `[parent, left, right]` and the postorder is `[left, right, parent]`. 
If we pop the parent from postorder, then postorder is `[left, right]` and this coincides to 
preorder except the first `[parent]`. To generalize, if there exists another depth, we use DFS.

## Approach
**Step-by-Step Process**

1. Pop the parent `node` from `postorder`.

2. If there exists another depth, then `node.val` doesn't match to `preorder` branch.
    - Extend the right branch with iterating DFS.
    - Same to the left branch.

3. If every middle elements are filled, then remove the last `parent` of `preorder`.
  
## Solutions
```python
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
