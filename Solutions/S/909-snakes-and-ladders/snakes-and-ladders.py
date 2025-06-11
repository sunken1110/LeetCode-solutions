#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/snakes-and-ladders/description

# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatten = [0]* (n*n)

        for i in range(n-1, -1, -2):
            for j in range(n):
                flatten[(n-1-i) * n + j] = board[i][j]

                if i >= 1:
                    flatten[(n-i) * n + (n-1-j)] = board[i-1][j]

        visited = [-1] * (n*n)
        queue = deque([0])
        visited[0] = 0

        while queue:
            pos = queue.popleft()

            if pos == n*n-1:
                return visited[pos]

            max_move = min(6, n*n-1-pos)

            for move in range(1, max_move+1):
                next_pos = pos + move

                if flatten[next_pos] != -1:
                    next_pos = flatten[next_pos] - 1

                if visited[next_pos] != -1:
                    continue

                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)

        return -1
