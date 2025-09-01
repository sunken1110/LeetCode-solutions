**Valid Sudoku**
=
[Problem Link](https://leetcode.com/problems/valid-sudoku/description)

## Intuition
A valid sudoku has three constraints; no repetition in each row, column, and square(block). For each constraint, we 
track the sets of integers to check if any repetition occurred. Note that the index of each square can be uniquely 
formulated by the index of row and the index of column.

## Approach
**Step-by-Step Process**

1. Initialize the set of integers in each row, col, and square as `rows`, `cols`, and `squares`, respectively.

2. Scan every value of `board` and update `rows`, `cols`, and `squares`.
    - An index of a square can be formulated as `i//3 * 3 + j//3` where `i`, `j` are the indices of row, column.
    - If any repetition occurred, then return False.
  
## Solutions
```python
# Time Complexity O(9^2), Space Complexity O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                idx = i//3 * 3 + j//3
                if num in squares[idx]:
                    return False
                squares[idx].add(num)

        return True
```
