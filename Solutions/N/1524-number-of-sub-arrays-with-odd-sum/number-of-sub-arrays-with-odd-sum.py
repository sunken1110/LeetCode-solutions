#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description

# Complexity O(n)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_cnt = 0
        even_cnt = 1
        cum_sum = 0
        cnt = 0

        for num in arr:
            cum_sum += num

            if cum_sum % 2 == 0:
                even_cnt += 1
                cnt += odd_cnt
            else:
                odd_cnt += 1
                cnt += even_cnt

        return cnt % (10**9 + 7)
