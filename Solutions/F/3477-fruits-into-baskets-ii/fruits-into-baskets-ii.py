#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/fruits-into-baskets-ii/description

# Time Complexity O(n*m), Space Complexity O(1)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        cnt = 0

        for fruit in fruits:
            for j in range(n):
                if fruit <= baskets[j]:
                    cnt += 1
                    baskets[j] = 0
                    break

        return n-cnt
