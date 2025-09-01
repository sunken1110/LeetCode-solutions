#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/valid-sudoku/description

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
