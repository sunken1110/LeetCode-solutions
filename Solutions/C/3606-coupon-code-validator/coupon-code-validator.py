#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/coupon-code-validator/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(s):
            if len(s) == 0:
                return False

            s = s.replace('_', '')

            return s.isalnum() or s == ''


        order = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        val = []

        for c, b, i in zip(code, businessLine, isActive):
            if is_valid(c) and (b in order) and i:
                val.append((order[b], c))

        val.sort()

        return [c for _, c in val]
