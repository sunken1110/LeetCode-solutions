#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/push-dominoes/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = list(dominoes)
        last_right = -1
        last_left = 0

        for idx, char in enumerate(dominoes):
            if char == 'R':
                if last_right != -1:
                    for i in range(last_right, idx):
                        ans[i] = 'R'

                last_right = idx

            elif char == 'L':
                if last_right != -1:
                    l, r = last_right, idx

                    while l < r:
                        ans[l], ans[r] = 'R', 'L'
                        l += 1
                        r -= 1

                    last_right = -1

                else:
                    for i in range(last_left, idx):
                        ans[i] = 'L'

                last_left = idx

        if last_right != -1:
            for i in range(last_right, n):
                ans[i] = 'R'

        return ''.join(ans)
