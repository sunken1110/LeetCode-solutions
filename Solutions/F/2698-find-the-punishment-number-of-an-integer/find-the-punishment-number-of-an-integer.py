#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description

# Time Complexity O(n*2^log(x, 10)), Space Complexity O(log(x, 10))
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(x, target):
            if x == target:
                return True

            if x == 0:
                return target == 0

            for div in (10, 100, 1000):
                if partition(x // div, target - x % div):
                    return True

            return False

        ans = 0

        for i in range(1, n+1):
            if partition(i*i, i):
                ans += i*i

        return ans
