**Set Matrix Zeroes**
=
[Problem Link](https://leetcode.com/problems/set-matrix-zeroes/description)

## Intuition
First, scan whole grid and store the coordinate in `pos` if the value is zero. Next, for each coordinate pair in `pos`, 
make the corresponding row and column to be all zeroes.

## Approach
**Step-by-Step Process**

1. Store every coordinate `(i, j)` in `pos = set()` if `matrix[i][j] = 0`.

2. For each coordinate pair in `pos`, make the corresponding row and column to be all zeroes in-place.
  
## Solutions
```python
# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        pos = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos.add((i, j))

        for i, j in pos:
            matrix[i] = [0] * n
            
            for row in matrix:
                row[j] = 0
```
