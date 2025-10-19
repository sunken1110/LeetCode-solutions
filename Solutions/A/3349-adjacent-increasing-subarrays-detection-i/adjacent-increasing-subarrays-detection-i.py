#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l, r = 0, 0
        prev = -inf

        for num in nums:
            if num > prev:
                r += 1

            else:
                if (l >= k and r >= k) or (r >= 2*k):
                    return True

                l, r = r, 1
                
            prev = num

        return (l >= k and r >= k) or (r >= 2*k)
