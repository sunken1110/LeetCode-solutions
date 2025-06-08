#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/lexicographical-numbers/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        i = 1

        while len(ans) < n:
            ans.append(i)

            if 10*i <= n:
                i *= 10

            else:
                while i % 10 == 9 or i == n:
                    i //= 10
                
                i += 1

        return ans
