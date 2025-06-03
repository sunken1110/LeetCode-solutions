#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/candy/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1

        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candies[i] = max(candies[i+1] + 1, candies[i])

        return sum(candies)
