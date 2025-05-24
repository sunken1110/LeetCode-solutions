#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        xor_diff = []

        for num in nums:
            ans += num
            xor = num ^ k
            xor_diff.append(xor - num)

        xor_diff.sort(reverse=True)

        for i in range(0, len(xor_diff)-1, 2):
            if xor_diff[i] + xor_diff[i+1] <= 0:
                break

            ans += xor_diff[i] + xor_diff[i+1]

        return ans
