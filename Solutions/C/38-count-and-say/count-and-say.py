#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-and-say/description

# Time Complexity O(2^n), Space Complexity O(2^n)
class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'

        if n == 1:
            return curr

        for _ in range(2, n+1):
            n_len = len(curr)
            s = ''
            cnt = 1
            char = curr[0]

            for i in range(1, n_len):
                if char != curr[i]:
                    s += str(cnt) + char
                    char = curr[i]
                    cnt = 1

                else:
                    cnt += 1

            s += str(cnt) + char
            curr = s

        return curr
