#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0

        for op in operations:
            if '++' in op:
                cnt += 1

            else:
                cnt -= 1

        return cnt
