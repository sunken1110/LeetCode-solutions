**Largest Color Value in a Directed Graph**
=
[Problem Link](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description)

## Intuition
We apply Kahn's algorithm for the topological sort of graph. While following the `node` with zero indegree, 
store the count of each `color` in `color_cnt[node][color]` along the current path. When we preceed to next node, 
renew `cnt` and update the color value.

## Approach
**Step-by-Step Process**

1. Connect edges in `graph` and set the indegrees of each node `indegree`.

2. To apply Kahn's algorithm, start the queue from the node with zero indegree.
    - To confirm the graph to be a DAG, follow the number of visited node `visited`

3. Store the count of each color along the path in `color_cnt`.
    - +1 to current color in `color_cnt` when visit a new node.
    - Update `color_value` of the current maximum color value.

4. For the adjacent nodes, update the path of maximum color for each color.

5. Repeat until we visit every node.
  
## Solutions
```python
# Time Complexity O(n + 26*e), Space Complexity O(26*n) where n is the number of nodes, e is the number of edges
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        visited = 0
        color_cnt = [[0] * 26 for _ in range(n)]
        color_value = 0
        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque(node for node in range(n) if indegree[node] == 0)

        while queue:
            node = queue.popleft()
            visited += 1
            color = ord(colors[node]) - ord('a')
            color_cnt[node][color] += 1
            color_value = max(color_value, color_cnt[node][color])

            for next_node in graph[node]:
                for c in range(26):
                    color_cnt[next_node][c] = max(color_cnt[next_node][c], color_cnt[node][c])

                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    queue.append(next_node)

        return color_value if visited == n else -1
```
