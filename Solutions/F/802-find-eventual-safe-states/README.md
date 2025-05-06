**Find Eventual Safe States**
=
[Problem Link](https://leetcode.com/problems/find-eventual-safe-states/description)

## Intuition
We use DFS to traverse connected nodes of `graph`. If a node is safe, then any other path reaches to it is also safe. 
For efficiency, we store the information of node in `safe` whether this node is safe or not. Then the task is as 
follows: while processing DFS, check `safe` and if the node is not searched yet then move to the next node. 
To avoid any looping, we check `visited` before traverse the next node and if the path reaches to the original node, 
then we can conclude that this is not a safe node.

## Approach
**Step-by-Step Process**

1. Initialize `safe` as -1s which stores the safe information of each node, and `visited` for avoiding any loop.

2. Define DFS.
    - Check `safe` first to prevent unnecessary traverse if we already searched.
    - To avoid any loop, if the current node is in `visited`, then return `False`.
    - If still undecided, then move to the next node.

3. For each node of `graph`, process DFS.
  
## Solutions
```python
# Time Complexity O(v+e) where v is the number of nodes and e is the number of edges
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [-1] * n
        visited = set()
        ans = []


        def dfs(node):
            if safe[node] == 1 or len(graph[node]) == 0:
                return True

            if safe[node] == 0 or node in visited:
                return False

            visited.add(node)

            for next_node in graph[node]:
                if not dfs(next_node):
                    safe[next_node] = 0
                    return False

            safe[node] = 1

            return True

        
        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
