#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/rearranging-fruits/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter(basket1)

        for x in basket2:
            freq[x] -= 1

        swap = []

        for fruit, cnt in freq.items():
            if cnt % 2 == 1:
                return -1

            diff = abs(cnt // 2)
            swap += [fruit] * diff

        swap.sort()
        min_val = min(basket1 + basket2)
        cost = 0

        for i in range(len(swap) // 2):
            cost += min(swap[i], 2*min_val)

        return cost
