#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description

# Complexity O(n*log*n))
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(capability):
            cnt = 0
            idx = 0

            while idx < len(nums):
                if nums[idx] <= capability:
                    cnt += 1
                    idx += 2

                else:
                    idx += 1

            return cnt >= k

        
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        return left
