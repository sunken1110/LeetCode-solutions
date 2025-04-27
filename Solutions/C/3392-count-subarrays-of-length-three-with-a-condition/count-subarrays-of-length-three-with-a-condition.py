#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums)-2):
            if 2*(nums[i]+nums[i+2]) == nums[i+1]:
                cnt += 1
            
        return cnt
