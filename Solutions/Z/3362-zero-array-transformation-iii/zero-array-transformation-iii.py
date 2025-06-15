#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/zero-array-transformation-iii/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        max_heap = []
        curr = 0
        pref = [0] * (n+1)
        
        queries.sort(key=lambda x: -x[0])

        for idx, num in enumerate(nums):
            while queries and idx == queries[-1][0]:
                heappush(max_heap, -queries.pop()[1])
                
            curr += pref[idx]

            while max_heap and idx <= -max_heap[0] and num > curr:
                curr += 1
                pref[-heappop(max_heap) + 1] -= 1
            
            if num > curr:
                return -1

        return len(max_heap)
