#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description

# Time Complexity O(2^n), Space Complexity O(n)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)
        n = len(nums)

        def rec(i, curr):
            if i == n:
                return curr == max_or

            take = rec(i + 1, curr | nums[i])
            skip = rec(i + 1, curr)

            return take + skip

        return rec(0, 0)
