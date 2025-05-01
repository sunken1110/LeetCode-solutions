#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        left = 0
        check = 0
        cnt = 0

        for right in range(len(nums)):
            if nums[right] == target:
                check += 1

            while check >= k:
                if nums[left] == target:
                    check -= 1

                left += 1

            cnt += left

        return cnt
