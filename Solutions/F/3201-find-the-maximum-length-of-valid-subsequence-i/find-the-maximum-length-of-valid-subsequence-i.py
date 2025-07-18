#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even = 0
        cnt_odd = 0
        cnt_alt_even = 0
        cnt_alt_odd = 0

        for num in nums:
            if num % 2 == 0:
                cnt_even += 1
                cnt_alt_even = cnt_alt_odd + 1

            else:
                cnt_odd += 1
                cnt_alt_odd = cnt_alt_even + 1

        return max(cnt_even, cnt_odd, cnt_alt_even, cnt_alt_odd)
