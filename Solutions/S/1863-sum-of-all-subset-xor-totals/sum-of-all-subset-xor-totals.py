#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description

# Time Complexity O(2^n), Space Complexity O(n)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0


        def backtrack(i, curr):
            if i == len(nums):
                self.ans += curr
                return

            backtrack(i + 1, curr)
            backtrack(i + 1, curr ^ nums[i])

        
        backtrack(0, 0)

        return self.ans
