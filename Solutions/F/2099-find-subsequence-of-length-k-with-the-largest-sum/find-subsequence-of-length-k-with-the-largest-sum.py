#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))

        return [num for num, _ in sorted(sorted_nums[-k:], key=lambda x: x[1])]
