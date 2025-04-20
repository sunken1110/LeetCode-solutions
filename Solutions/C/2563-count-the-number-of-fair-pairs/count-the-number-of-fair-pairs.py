#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-fair-pairs/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()


        def count(num):
            left = 0
            right = n-1
            cnt = 0

            while left < right:
                if nums[left] + nums[right] <= num:
                    cnt += (right-left)
                    left += 1

                else:
                    right -= 1

            return cnt


        return count(upper)- count(lower-1)
