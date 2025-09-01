**Sudoku Solver**
=
[Problem Link](https://leetcode.com/problems/sudoku-solver/description)

## Intuition
We store integer sets of each row, col, and squares to check if a sudoku is valid. The basic approach follows:

[Problem Link](https://leetcode.com/problems/valid-sudoku/description)

To solve the sudoku, we need to feel each empty cell with at least one integer. We don't know if each cell is valid or 
not until we see any repetition within the row, column, and square that contains this cell. So we need to check 
every case, and the backtracking is a good approach here. When we meet any empty cell, fill it with any integer from 
1 to 9 and check the row, column, and square which contains this cell. If no duplication occurred, then move to the next 
cell and repeat the process. Check every case until a valid sudoku is found.

## Approach
**Step-by-Step Process**

1. Initialize the sets of integer `rows`, `cols`, and `squares`.

2. First, scan every cell and fill `rows`, `cells`, and `squares`. Also store the index of empty cells `empties`.

3. Construct a backtracking.
    - Start from the first empty cell.
    - Fill it with non-duplicated value and move to the next empty cell.
    - Repeat the process until we find a valid sudoku.
    - If any duplication is found, then go back and change the value of previously filled cell.
  
## Solutions
```python
# Time Complexity O(9^n), Space Complexity O(9^2)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))

                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[(i//3) * 3 + j//3].add(num)


        def backtracking(idx):
            if idx == len(empties):
                return True

            i, j = empties[idx]
            k = (i//3) * 3 + j//3

            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in squares[k]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[k].add(num)

                    if backtracking(idx+1):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    squares[k].remove(num)

            return False


        backtracking(0)
```
