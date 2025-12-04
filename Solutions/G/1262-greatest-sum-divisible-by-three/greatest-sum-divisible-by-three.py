#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/greatest-sum-divisible-by-three/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        one1, one2, two1, two2 = inf, inf, inf, inf
        min_remove = inf

        for num in nums:
            total += num

            if num % 3 == 1:
                if num < one1:
                    one2 = one1
                    one1 = num

                elif num < one2:
                    one2 = num

            elif num % 3 == 2:
                if num < two1:
                    two2 = two1
                    two1 = num

                elif num < two2:
                    two2 = num

        if total % 3 == 0:
            return total

        elif total % 3 == 1:
            if one1 != inf:
                min_remove = min(min_remove, one1)

            if two2 != inf:
                min_remove = min(min_remove, two1 + two2)

        else:
            if two1 != inf:
                min_remove = min(min_remove, two1)

            if one2 != inf:
                min_remove = min(min_remove, one1 + one2)

        return total - min_remove
