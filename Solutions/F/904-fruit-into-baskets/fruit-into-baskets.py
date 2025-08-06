#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/fruit-into-baskets/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        max_cnt = 0

        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            max_cnt = max(max_cnt, r-l+1)

        return max_cnt
