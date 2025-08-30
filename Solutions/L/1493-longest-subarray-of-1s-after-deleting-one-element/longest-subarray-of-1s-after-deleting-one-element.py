#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        prev_len = 0
        check = False

        for num in nums:
            if num:
                curr_len +=1

            else:
                prev_len = curr_len
                curr_len = 0
                check = True

            max_len = max(max_len, prev_len + curr_len)

        return max_len if check else len(nums)-1
