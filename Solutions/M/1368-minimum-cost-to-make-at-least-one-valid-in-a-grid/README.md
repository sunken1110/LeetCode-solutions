**Minimum Cost to Make at Least One Valid In a Grid**
=
[Problem Link](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description)

## Intuition
We have to connect at least one valid path and the minimum cost of it. We use BFS by traveling the grid along the original trace
and expand the trace by connecting adjacent grids with `cost + 1` until we reach the destination.
If we don't reach `[m-1, n-1]` yet, then now travel expanded not-visited grids of `cost + 1` and repeat over and over.

## Approach
**Step-by-Step Process**

1. Set the direction lists. Note that `grid[i][j]` starts from 1 not 0.

2. Start traveling from the original point `not_visited = deque([x=0, y=0, cost=0])` along the given trace.
    - While traveling, mark every visited grid as `cost` since we can access freely.

3. Record not-visited adjacent grids as `cost + 1` and append to `not_visited`.
    - **Caution** : If an adjacent grid along the trace that will be reached by traveling, it automatically will be marked as `cost`.
  
4. If we are not at the destination yet, repeat step 2 with `cost + 1` grids.

5. Finish the process if we reach the `grid[m-1][n-1]`.
  
## Solutions
```python
# Complexity O(m*n)
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        costs = {}
        not_visited = deque([[0, 0, 0]])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 1: right, 2: left, 3: up, 4: down

        while not_visited:
            x, y, cost = not_visited.popleft()

            while 0 <= x < m and 0 <= y < n and (x, y) not in costs:
                costs[x, y] = cost
                
                for d in directions:
                    not_visited.append([x + d[0], y + d[1], cost + 1]) # if 

                dx, dy = directions[grid[x][y] - 1] # index adjust

                x += dx
                y += dy

        return costs[m-1, n-1]
```
