**Maximum Number of Points From Grid Queries**
=
[Problem Link](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description)

## Intuition
For each query, the task is a straightforward BFS problem. However, run BFS several times may lead to the time limit, 
we need more efficient approach. Note that as the value of `queries` increases, the available area of grid also 
increases. Moreover, the area of smaller query value is a subset of the area of bigger query value. 
In this point, we sort `queries` in increasing order and run a BFS until all neighbor cells meet the value of 
first query. Then return the current points, and continue BFS until the next value of query.

## Approach
**Step-by-Step Process**

1. Sort `queries` in increasing order.
    - Store indices of each query to recover the order of answer.

2. To run a BFS with bounded value, we use a min heap `queue`.

3. For each value of `queries`, run a BFS until every neighbor meets the value of query.
    - If finished, then return the total points to `ans` in correct order.
  
4. Move BFS on to the next value of query.
  
## Solutions
```python
# Time Complexity O(mn + q*log(q))
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        ans = [0] * len(queries)
        pts = 0

        for val, idx in queries:
            while queue and queue[0][0] < val:
                pts += 1
                v, x, y = heappop(queue)

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heappush(queue, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True

            ans[idx] = pts

        return ans
```
