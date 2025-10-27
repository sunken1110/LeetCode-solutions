#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        w, d = divmod(n, 7)
        
        return 28*w + 7*w*(w-1)//2 + d*(d+1)//2 + w*d
