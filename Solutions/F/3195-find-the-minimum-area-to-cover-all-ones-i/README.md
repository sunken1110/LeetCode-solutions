**Find the Minimum Area to Cover All Ones I**
=
[Problem Link](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description)

## Intuition
Since we have to cover the ones with rectangular shape, the target rectangle is decided by the maximum right, 
minimum left, maximum bottom and minimum top.

## Approach
**Step-by-Step Process**

1. Initialize `bottom`, `top`, `left`, and `right` which refer the indices of edge.

2. Scan every element in `grid`.
    - `left` is the minimum left index of one, and `right` is the maximum index of one in each row.
    - Similarly `bottom` and `top` can be decided.

3. Return the area of the target rectangle.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        bottom, top, left, right = len(grid), -1,len(grid[0]), -1

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col:
                    bottom = min(bottom, i)
                    top = max(top, i)
                    left = min(left, j)
                    right = max(right, j)

        return (top-bottom+1) * (right-left+1)
