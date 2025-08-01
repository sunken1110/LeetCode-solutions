#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/bitwise-ors-of-subarrays/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev = set()

        for num in arr:
            curr = {num}

            for i in prev:
                curr.add(i|num)

            ans.update(curr)
            prev = curr

        return len(ans)
