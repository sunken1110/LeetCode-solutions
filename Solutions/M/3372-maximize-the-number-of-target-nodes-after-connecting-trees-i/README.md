**Maximize the Number of Target Nodes After Connecting Trees I**
=
[Problem Link](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description)

## Intuition
Note that the node of `edge2` which directly to be connected to `edge1` is uniquely determined (can be multiple nodes). 
To see this fact, a connection between two trees require 1 edge and consequently the target nodes are new target nodes
of path length `k-1` in `edge2`. Since it is independent to the first tree, we only need to find the maximum value of it. 
Therefore, if we construct `dfs(node, depth)` a DFS algorithm which count the number of target nodes for each `node` 
then the task is to calculate `dfs(node1, k) + max(dfs(node2, k-1))` where `node1`, `node2` are nodes in `edge1`, `edge2`, 
respectively.

## Approach
**Step-by-Step Process**

1. Construct a DFS algorithm.
    - Until the depth does not exceed `k`, search deeply and count the visited nodes.
  
2. Find the maximum DFS `max2` of the second tree with path length `k-1`.

3. For each node in the first tree, compute DFS value of path length `k` and add to `max2`.
  
## Solutions
```python
# Time Complexity O((m+n)*k), Space Complexity O(m+n)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, parent, depth, graph, cnt=1):
            if depth < k:
                for next_node in graph[node]:
                    if next_node == parent:
                        continue

                    cnt += dfs(next_node, node, depth+1, graph)

            return cnt


        m = len(edges1) + 1
        n = len(edges2) + 1

        if k == 0:
            return [1] * m

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        max2 = 0
        for node in range(n):
            max2 = max(max2, dfs(node, -1, 1, graph2))

        return [dfs(node, -1, 0, graph1) + max2 for node in range(m)]
```
