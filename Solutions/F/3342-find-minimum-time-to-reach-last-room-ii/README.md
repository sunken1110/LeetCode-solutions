**Find Minimum Time to Reach Last Room II**
=
[Problem Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description)

## Intuition
This problem is a twisted version of the following:
[Problem Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description)

With the exact same approach, we add additional `v` to the `queue` which refers an alternating moving time. 

## Approach
**Step-by-Step Process**

1. Initialize the minimum times to reach `(i, j)` room as `times[i][j]`.

2. Construct a Dijkstra's algorithm with priority queue.
    - Pop `(x, y, v)` from the priority queue.
    - With 4 directions, check `(nx, ny)` is an available room.
    - If the minimum time to move room `(nx, ny)` is faster than previous visits, then append to the queue.
    - Alternate `v` when appending a new queue.
    - Repeat until reach to the room `(m-1, n-1)`.
  
## Solutions
```python
# Time Complexity O(m*n*log(m*n)), Space Complexity O(m*n)
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        times = [[inf] * n for _ in range(m)]
        times[0][0] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = [(0, 0, 0, 1)]

        while queue:
            t, x, y, v = heapq.heappop(queue)

            if x == m-1 and y == n-1:
                return t

            if t > times[x][y]:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nt = max(moveTime[nx][ny], t) + v

                    if times[nx][ny] > nt:
                        times[nx][ny] = nt
                        nq = (nt, nx, ny, 2) if v == 1 else (nt, nx, ny, 1)
                        heapq.heappush(queue, nq)
```
