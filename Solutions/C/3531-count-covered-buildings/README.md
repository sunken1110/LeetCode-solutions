**Count Covered Buildings**
=
[Problem Link](https://leetcode.com/problems/count-covered-buildings/description)

## Intuition
Note that a covered building has 4 covering buildings in all four directions. That is, if we mark every 
maximum and minimum of each row and column, both `x` and `y` coordinates of a covered building must be 
located between them. We first scan every coordinate of `buildings` and update the maximum and minimum 
of each row and column. Then we check if a `building` with coordinate `(x, y)` is in-between  

## Approach
**Step-by-Step Process**

1. Initialize `max_x`, `min_x`, `max_y`, and `min_y`, which refer each row/column's max/min values.

2. Scan `buildings` and mark every maximum and minimum value of each row and column.

3. In the secondary scan, a building `(x, y)` is covered if `min_x[y] < x < max_x[y]` and vice versa. 
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_x = [0] * (n+1)
        min_x = [n+1] * (n+1)
        max_y = [0] * (n+1)
        min_y = [n+1] * (n+1)
        cnt = 0

        for x, y in buildings:
            max_x[y] = max(max_x[y], x)
            min_x[y] = min(min_x[y], x)
            max_y[x] = max(max_y[x], y)
            min_y[x] = min(min_y[x], y)

        for x, y in buildings:
            if min_x[y] < x < max_x[y] and min_y[x] < y < max_y[x]:
                cnt += 1

        return cnt
```
