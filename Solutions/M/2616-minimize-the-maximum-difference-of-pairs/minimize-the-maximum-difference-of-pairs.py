#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l+r) // 2
            idx = 0
            cnt = 0

            while idx < n-1:
                if nums[idx+1] - nums[idx] <= mid:
                    cnt += 1
                    idx += 1

                idx += 1

            if cnt >= p:
                r = mid

            else:
                l = mid + 1

        return l
