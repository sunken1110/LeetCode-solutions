#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2 == 1 or corridor.count('S') == 0:
            return 0

        num_s, num_p = 0, 0
        cnt = 1
        mod = 10**9 + 7

        for w in corridor:
            if w == 'S':
                if num_s == 2:
                    cnt = cnt * (num_p + 1) % mod
                    num_s, num_p = 0, 0

                num_s += 1

            else:
                if num_s == 2:
                    num_p += 1

        return cnt
