#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-time-to-repair-cars/description

# Complexity O(n*log(n))
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(minute):
            done = 0

            for rank, mechanic in ranks.items():
                done += mechanic * int(sqrt(minute / rank))

            return done >= cars

        ranks = Counter(ranks)
        left = 0
        right = max(ranks) * ceil(cars / len(ranks))**2

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        return left
