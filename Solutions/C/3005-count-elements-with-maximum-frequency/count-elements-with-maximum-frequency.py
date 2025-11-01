#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-elements-with-maximum-frequency/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        ans = 0

        for val in freq.values():
            if val == max_freq:
                ans += val

        return ans
