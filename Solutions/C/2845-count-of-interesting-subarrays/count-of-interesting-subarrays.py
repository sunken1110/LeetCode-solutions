#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-of-interesting-subarrays/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        cnt = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1

            curr = prefix % modulo
            gap = (modulo + curr - k) % modulo
            cnt += freq[gap]
            freq[curr] += 1

        return cnt
