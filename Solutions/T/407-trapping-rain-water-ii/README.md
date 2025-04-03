**Trapping Rain Water II**
=
[Problem Link](https://leetcode.com/problems/tuple-with-same-product/description)

## Intuition
The cell filled by water implies that the neighbor cells are much higher than it. Moreover, the height must be 
equal to the lowest neighbor's height. The idea is to use a min heap to fill lower cell first and then fill 
higher cell. Note that the boundary cells cannot be filled by water, so the initial state must be the boundary.

## Approach
**Step-by-Step Process**

1. To avoid any multiple searchs, define `visited`.

2. Visit every boundary and push to the min heap `queue`.
    - `visited` must be changed to `True` on these cells.

3. Fill the lowest cells first and add to the total volume of water.
    - The height is the difference between `heightMap[i][j]` and the lowest neighbor cell's height.
  
4. Now, filled cells work as solid neighbor cells. Push filled cells to the `queue` and repeat.
  
## Solutions
```python
# Complexity O(mn*log(mn)))
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        queue = []
        vol = 0

        for i in range(m):
            for j in [0, n-1]:
                heappush(queue, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(1, n-1):
            for i in [0, m-1]:
                heappush(queue, (heightMap[i][j], i, j))
                visited[i][j] = True

        while queue:
            h, x, y = heappop(queue)

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    vol += max(0, h - heightMap[nx][ny])
                    visited[nx][ny] = True

                    heappush(queue, (max(h, heightMap[nx][ny]), nx, ny))

        return vol
```
