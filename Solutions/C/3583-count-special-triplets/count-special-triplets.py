#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-special-triplets/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        lefts = Counter()
        rights = Counter(nums)
        total = 0
        mod = 10**9 + 7

        for num in nums:
            rights[num] -= 1
            total = (total + lefts[num*2] * rights[num*2]) % mod
            lefts[num] += 1

        return total
