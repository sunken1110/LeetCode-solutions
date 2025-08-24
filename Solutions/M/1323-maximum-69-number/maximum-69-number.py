#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-69-number/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = list(str(num))

        for i in range(len(ans)):
            if ans[i] == '6':
                ans[i] = '9'

                return int(''.join(ans))

        return int(''.join(ans))
