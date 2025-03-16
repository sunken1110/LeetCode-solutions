#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description

# Complexity O(n*log(m))
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            cnt = sum(pile // mid for pile in candies)

            if cnt >= k:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans
