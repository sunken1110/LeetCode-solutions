**Making a Large Island**
=
[Problem Link](https://leetcode.com/problems/making-a-large-island/description)

## Intuition
We are given `n x n` grid with `0` water cell and `1` land cell. Also we can convert at most one water cell to land cell. 
Since our goal is to find the largest island after exact one operation, it is clear that this operation must be executed on the 
boundary of one specific island. Then, in the sense of target water cell, a potential size of expanded island is the sum of adjacent
island's sizes. Therefore, we cumulatively add each island's size to boundary water cells while traveling each island. 
The maximum value of water cells is the answer.

As an example, consider the following case:
||||||
|-|-|-|-|-|
|0|0|1|1|1|
|0|0|0|0|0|
|1|1|0|1|1|
|1|1|0|1|0|
|0|0|0|0|0|

Let's travel from the leftmost island clockwisely. If we find a land cell, then calculate a size of it. To avoid any duplication,
we mark visited cell as `-1` while traveling each island. After calculation, we add it to the boundary cells. 
The first operation yields:
||||||
|-|-|-|-|-|
|0|0|1|1|1|
|4|4|0|0|0|
|-1|-1|4|1|1|
|-1|-1|4|1|0|
|4|4|0|0|0|

The second operation yields:
||||||
|-|-|-|-|-|
|0|3|-1|-1|-1|
|4|4|3|3|3|
|-1|-1|4|1|1|
|-1|-1|4|1|0|
|4|4|0|0|0|

The last operation yields:
||||||
|-|-|-|-|-|
|0|3|-1|-1|-1|
|4|4|3|6|6|
|-1|-1|7|-1|-1|
|-1|-1|7|-1|3|
|4|4|0|3|0|

Two cells with maximal value `7` are our targets. Note that the total area is `7 + 1`, including the target itself.

## Approach
**Step-by-Step Process**

1. Find any land cell, then append to deque.
    - Initialize `area` to 1.
    - To memorize a potential area of each water cell after converting, set `potential_area = defaultdict(int)`.
    
2. To identify each island, we define a DFS function.
    - Move along 4 direction to adjacent land until visiting every cell.

3. After moving, mark previous land cell to `-1` to avoid any duplicated visit.\
    - Also `area += 1`.

4. Set `near_land` to note every adjacent water cells (boundary of island).

5. After traveling one island finished, add `area` to every boundary water cell in `potential_area`.

6. Repeat previous process until we visit every land cell in `grid`. 
  
## Solutions
```python
# Complexity O(m*n)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        potential_area = defaultdict(int)

        def dfs(node):
            q = deque([node])
            area = 1
            near_land = set()
            
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            q.append((nx, ny))
                            grid[nx][ny] = -1
                            area += 1

                        elif grid[nx][ny] == 0:
                            near_land.add((nx, ny))

            for water in near_land:
                potential_area[water] += area

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    grid[x][y] = -1
                    dfs((x, y))

        if potential_area:
            return 1 + max(potential_area.values())

        elif grid[0][0] == 0:
            return 1

        else:
            return m * n
```
