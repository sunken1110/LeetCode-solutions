**Diagonal Traverse**
=
[Problem Link](https://leetcode.com/problems/diagonal-traverse/description)

## Intuition
Note that the odd-indexed diagonal moves right and the even-indexed diagonal moves left. We traverse along 
the diagonal, and change the direction if we meet the boundary of `mat`. Check the direction of current diagonal, 
and change the direction if we meet the boundary.

## Approach
**Step-by-Step Process**

1. Start from the `row=0`, `col=0`.

2. The direction of diagonal can be checked by the parity of `row + col`.

3. If the traverse meet the boundary of `mat` and the direction have to be changed, move to the next diagonal.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        ans = []

        for _ in range(m*n):
            ans.append(mat[row][col])

            if (row + col) % 2 == 0:
                if col == n-1:
                    row += 1

                elif row == 0:
                    col += 1

                else:
                    row -= 1
                    col += 1

            else:
                if row == m-1:
                    col += 1

                elif col == 0:
                    row += 1

                else:
                    row += 1
                    col -= 1

        return ans
```
