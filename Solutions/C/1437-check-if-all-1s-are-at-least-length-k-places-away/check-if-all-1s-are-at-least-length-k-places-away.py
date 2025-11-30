#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        
        start = nums.index(1)
        curr = 0

        for num in nums[start+1:]:
            if num == 0:
                curr += 1

            else:
                if curr < k:
                    return False

                curr = 0

        return True
