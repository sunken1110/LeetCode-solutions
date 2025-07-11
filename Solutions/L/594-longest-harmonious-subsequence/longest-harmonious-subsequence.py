#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-harmonious-subsequence/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in freq:
            if freq[num+1]:
                max_len = max(max_len, freq[num] + freq[num+1])

        return max_len
