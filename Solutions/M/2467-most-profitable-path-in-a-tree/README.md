**Most Profitable Path in a Tree**
=
[Problem Link](https://leetcode.com/problems/most-profitable-path-in-a-tree/description)

## Intuition
Note that Bob's path is always fixed. We first find a parent of each node. Secondly, we traverse Bob's 
path and construct a list that stores how many steps are needed to reach each node. Finally, we define 
DFS to compute every net income of Alice of each branches. In this step, if Alice's path is overwrapped 
to Bob's path, we adjust income as defined.

## Approach
**Step-by-Step Process**

1. Define `graph` to identify connected edges.

2. With `graph`, we find each node's parent and child nodes. This can be implemented by using DFS.

3. Traverse Bob's walkthrough. For each step, we store each nodes with required steps in `bob_arrival`.

4. Finally, again construct a DFS algorithm with respect to Alice.
    - If Alice's path is overwrapped to Bob's, adjust the income of overwrapped node with `bob_arrival`.
    - If Alice reach to a leaf, return maximum net income. Traverse every branch.

## Solutions
```python
# Complexity O(n)
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        bob_arrival = [inf] * n
        parents = [-1] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        #--------------------------------

        def link_nodes(node, parent):
            parents[node] = parent

            for child in graph[node]:
                if child == parent:
                    continue

                link_nodes(child, node)

        link_nodes(0, -1)

        #--------------------------------

        bob_loc = bob
        bob_step = 0

        while bob_loc != -1:
            bob_arrival[bob_loc] = bob_step
            bob_step += 1
            bob_loc = parents[bob_loc]

        #--------------------------------

        def dfs(node, step, parent):
            max_sum = -inf
            find_leaf = True

            if step < bob_arrival[node]:
                alice = amount[node]

            elif step == bob_arrival[node]:
                alice = amount[node]//2

            else:
                alice = 0


            for child in graph[node]:
                if child == parent:
                    continue

                find_leaf = False
                max_sum = max(max_sum, dfs(child, step + 1, node))

            return alice + max_sum if not find_leaf else alice

        return dfs(0, 0, -1)
```
