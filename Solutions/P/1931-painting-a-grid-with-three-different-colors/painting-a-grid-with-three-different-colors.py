#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description

# Time Complexity O((m+n)*k^2), Space Complexity(O(k^2)) where k is len(num_seq)
class Solution(object):
    def colorTheGrid(self, m, n):
        def dfs(idx, prev_color, seq):
            if idx == m:
                candidates.append(seq)
                
                return

            for color in range(3):
                if color != prev_color:
                    dfs(idx+1, color, seq*3 + color)


        candidates = []
        mod = 10**9 + 7

        dfs(0, -1, 0)
        num_seq = len(candidates)
        neighbors = [[] for _ in range(num_seq)]

        for i, seq1 in enumerate(candidates):
            for j, seq2 in enumerate(candidates):
                x, y = seq1, seq2
                check = True

                for _ in range(m):
                    if x % 3 == y % 3:
                        check = False
                        break

                    x //= 3
                    y //= 3

                if check:
                    neighbors[i].append(j)

        dp = [1] * num_seq

        for _ in range(n-1):
            dp2 = [0] * num_seq

            for i in range(num_seq):
                if dp[i]:
                    for j in neighbors[i]:
                        dp2[j] = (dp2[j] + dp[i]) % mod

            dp = dp2

        return sum(dp) % mod
