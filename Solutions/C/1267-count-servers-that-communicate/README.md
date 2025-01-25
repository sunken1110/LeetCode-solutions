**Count Servers that Communicate**
=
[Problem Link](https://leetcode.com/problems/count-servers-that-communicate/description)

## Intuition
Two servers can communicate if they are in same row or column. To check the connectivity, we construct a matrix 
that each grid counts the number of servers in same row or column. Since the connectivity only depends on the row or the column,
we just consider the total sum of each rows(columns). After complete the matrix, we check
if there exists other communicating server in the view of fixed server.

## Approach
**Step-by-Step Process**

1. Construct a communicating matrix.
    - In the sense of rows and columns, we need 2 matrices namely `rows` and `cols`.
  
2. For each rows and columns, count the number of servers in 1) same row and 2) same column.

3. Again for each rows and columns, count the number of communicate servers.
  
## Solutions
```python
# Complexity O(m*n)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1)):
                    cnt += 1
        
        return cnt
```
