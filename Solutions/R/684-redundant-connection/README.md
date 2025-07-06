**Redundant Connection**
=
[Problem Link](https://leetcode.com/problems/redundant-connection/description)

## Intuition
Suppose there is a cycle, then the roots of each node coincide. We use union-find algorithm to find each node, and if 
the roots of two nodes in edge equal, return it.

## Approach
**Step-by-Step Process**

1. Initialize the roots `root`.

2. Define a union-find algorithm and find roots of two nodes of each `edge`.
    - If two roots coincide, return two nodes.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1))

        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node])

            return root[node]

        for node1, node2 in edges:
            root1, root2 = find_root(node1), find_root(node2)

            if root1 == root2:
                return [node1, node2]

            root[root2] = root1
