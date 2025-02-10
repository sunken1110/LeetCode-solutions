#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/tuple-with-same-product/description

# Complexity O(n)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]

                if prod in count:
                    count[prod] += 1
                else:   
                    count[prod] = 1

        for prod, freq in count.items():
            ans += freq * (freq - 1) * 4

        return ans
