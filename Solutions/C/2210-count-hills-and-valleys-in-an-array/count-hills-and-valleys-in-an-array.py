#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = -1
        prev = nums[0]
        diff = 0
        curr_diff = 0

        for num in nums[1:]:
            if num - prev > 0:
                curr_diff = 1

            elif num - prev < 0:
                curr_diff = -1

            if diff != curr_diff:
                cnt += 1

            diff = curr_diff
            prev = num

        return max(0, cnt)
