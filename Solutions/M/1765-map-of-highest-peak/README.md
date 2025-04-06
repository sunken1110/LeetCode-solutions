**Map of Highest Peak**
=
[Problem Link](https://leetcode.com/problems/map-of-highest-peak/description)

## Intuition
We start from the flat ground, and then pile up the land starts from the water cell and then neighbors. 
The most tricky part is the following scenario:

1. Starts from at least 2 water cell, and increase the height of neighbor cells.

2. At some point, the cells which have to be heightened coincide.

3. However the heights originated from different water cell differ at least 2, so the height continuity cannot be hold.

To avoid this problem, we use `deque` structure. Process every water cells simultaneously and then move to the 
neighbors, and repeat it.

## Approach
**Step-by-Step Process**

1. Set the heights of cell to be all -1 (flatten).

2. Initialize the heights of water cells to be 0, and store x, y coordinates with height to `visit`.

3. For every water cell, check available neighbor land cell and heighten it by 1.
    - To avoid the mentioned problem, use `popleft()` of deque.

4. Repeat until every height of cells are not -1.
  
## Solutions
```python
# Time Complexity O(n)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        heights = [[-1] * n for _ in range(m)]
        visited = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    visited.append((i, j, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while visited:
            x, y, h = visited.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = h+1
                    visited.append((nx, ny, h+1))

        return heights
```
