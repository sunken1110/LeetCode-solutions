#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-number-of-bad-pairs/description

# Complexity O(n)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        new_nums = [nums[i] - i for i in range(n)]

        freq = Counter(new_nums)

        for cnt in freq.values():
            ans += cnt * (cnt-1) // 2

        return (n * (n-1) // 2) - ans
