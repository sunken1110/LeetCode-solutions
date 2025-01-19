#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/neighboring-bitwise-xor/description

# Time Complexity O(n)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = reduce(operator.xor, derived)

        return bool(not ans)

# Time Complexity O(n)
class Solution2:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        return sum(derived) % 2 == 0
