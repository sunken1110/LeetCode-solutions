#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-index-of-a-valid-split/description

# Complexity O(n)
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dom_val, dom_cnt = max(Counter(nums).items(), key=lambda x: x[1])

        cnt = 0
        for i, num in enumerate(nums):
            if num == dom_val:
                cnt += 1

            if cnt > (i+1) // 2 and (dom_cnt - cnt) > (n-i-1) // 2:
                return i

        return -1
