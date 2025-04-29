#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        cnt = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr * (right-left+1) >= k:
                curr -= nums[left]
                left += 1

            cnt += right-left+1

        return cnt
