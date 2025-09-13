**Find the Minimum Area to Cover All Ones II**
=
[Problem Link](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description)

## Intuition
Since we cover `grid` with non-overlapping 3 rectangles, we first need to divide `grid` into three rectangular 
partitions. Suppose the first rectangle is decided by a vertical cut. Then the remained 2 rectangles can be 
partitioned by vertically or horizontally from the remained cut of `grid`. Note that the first rectangle also 
can be decided by a horizontal cut. To get every case, the smart approach is to use a rotation of `grid`. 
Always get the left vertical cut as a first rectangle, get 2 cases of remained rectangle. Now rotate the `grid` 
and get every possible partition as same as the previous way until we rotate 4 times, then we can get every 
possible partition. The remaining is to return the minimum sum of area, and we can use the algorithm of the 
following preliminary problem:

[Problem Link](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description)

The answer is the minimum of area sum.

## Approach
**Step-by-Step Process**

1. Define `rotate` which returns the rotated matrix.

2. Define `minArea` which returns the minimum area of rectangle that covers every 1 of given matrix.

3. For a given `grid`, get every possible 3-rectangle partition which divides `grid` completely.
    - First, get a rectangle divides `grid` vertically.
    - Secondly, for the remained 2 rectangles, get 2 possibilities of dividing vertically and horizontally.
    - Use `minArea` to get a minimum area sum.

4. Use `rotate` to change the position of initial rectangle.

5. Return the minimum area among all cases.
  
## Solutions
```python
# Time Complexity O(m^2*n^2), Space Complexity O(m*n)
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def rotate(mat):
            m = len(mat)
            n = len(mat[0])

            return [[mat[i][j] for i in range(m-1, -1, -1)] for j in range(n)]


        def minArea(mat):
            if not mat or not mat[0]:
                return 0

            m = len(mat)
            n = len(mat[0])
            top, bottom, left, right = -1, m, n, -1

            for i in range(m):
                for j in range(n):
                    if mat[i][j]:
                        top = max(top, i)
                        bottom = min(bottom, i)
                        left = min(left, j)
                        right = max(right, j)

            if right == -1:
                return 0

            return (right-left+1) * (top-bottom+1)


        ans = float('inf')

        for _ in range(4):
            m = len(grid)
            n = len(grid[0])

            for i in range(1, m):
                area1 = minArea(grid[:i])

                for j in range(1, n):
                    partition2 = [row[:j] for row in grid[i:]]
                    partition3 = [row[j:] for row in grid[i:]]
                    area2 = minArea(partition2)
                    area3 = minArea(partition3)
                    ans = min(ans, area1 + area2 + area3)

                for k in range(i+1, m):
                    partition2 = grid[i:k]
                    partition3 = grid[k:]
                    area2 = minArea(partition2)
                    area3 = minArea(partition3)
                    ans = min(ans, area1 + area2 + area3)

            grid = rotate(grid)

        return ans
```
