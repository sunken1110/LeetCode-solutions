**Increment Submatrices by One**
=
[Problem Link](https://leetcode.com/problems/increment-submatrices-by-one/description)

## Intuition
To efficiently compute the amount of each increment, we use 2D prefix sum. Sweep twice as row-wise and column-wise, 
and then adjust `-1` to duplicated area. 

## Approach
**Step-by-Step Process**

1. Initialize `pref_mat` as a 2D prefix sum array.
    - Note that the coordinate with `row >= row2 + 1` and `col >= col2 + 1` should be adjusted by `-1`.
  
2. For each `(row, col)`, fill `mat[row][col]` by subtracting two adjacent prefix sum of `pref_mat`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        pref_mat = [[0] * (n+1) for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            pref_mat[r1][c1] += 1
            pref_mat[r2+1][c1] -= 1
            pref_mat[r1][c2+1] -= 1
            pref_mat[r2+1][c2+1] += 1

        for row in range(n):
            for col in range(n):
                loc1 = 0 if row == 0 else mat[row-1][col]
                loc2 = 0 if col == 0 else mat[row][col-1]
                loc3 = 0 if (row == 0 or col == 0) else mat[row-1][col-1]
                mat[row][col] = pref_mat[row][col] + loc1 + loc2 - loc3

        return mat
```
