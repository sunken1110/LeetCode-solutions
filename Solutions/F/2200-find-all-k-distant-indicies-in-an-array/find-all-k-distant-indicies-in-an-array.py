#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        r = 0

        for idx, num in enumerate(nums):
            if num == key:
                l = max(r, idx-k)
                r = min(len(nums), idx+k+1)

                for i in range(l, r):
                    ans.append(i)

        return ans
