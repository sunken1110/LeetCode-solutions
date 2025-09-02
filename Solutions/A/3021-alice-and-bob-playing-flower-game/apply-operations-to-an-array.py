#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/alice-and-bob-playing-flower-game/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m*n) // 2
