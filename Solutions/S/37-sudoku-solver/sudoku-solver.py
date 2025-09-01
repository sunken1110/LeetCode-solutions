#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/sudoku-solver/description

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
