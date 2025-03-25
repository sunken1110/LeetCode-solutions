#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/closest-prime-numbers-in-range/description

# Complexity O((right-left) * sqrt(right))
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 1:
                return False

            for div in range(2, int(sqrt(num)) + 1):
                if num % div == 0:
                    return False

            return True
        
        ans = []
        prev = None

        for num in range(left, right + 1):
            if not is_prime(num):
                continue

            if not prev:
                prev = num
                continue

            diff = num - prev

            if diff <= 2:
                return [prev, num]

            if not ans or diff < ans[1] - ans[0]:
                ans = [prev, num]

            prev = num

        return [-1, -1] if not ans else ans
