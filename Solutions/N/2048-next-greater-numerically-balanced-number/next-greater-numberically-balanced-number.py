#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBalanced(num):
            freq = [0] * 10
            
            while num > 0:
                if num % 10 == 0:
                    return False

                freq[num % 10] += 1
                num //= 10

            return all(i == cnt for i, cnt in enumerate(freq) if cnt)


        n += 1

        while not isBalanced(n):
            n += 1

        return n
