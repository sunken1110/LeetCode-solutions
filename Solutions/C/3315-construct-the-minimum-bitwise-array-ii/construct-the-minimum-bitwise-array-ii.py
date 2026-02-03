#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            if n != 2:
                ans.append(n - ((n+1) & (-n-1)) // 2)

            else:
                ans.append(-1)
                
        return ans
