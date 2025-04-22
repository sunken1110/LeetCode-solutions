#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/rabbits-in-forest/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        ans = 0

        for val, cnt in freq.items():
            ans += (cnt+val) // (val+1) * (val+1)

        return ans
