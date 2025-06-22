#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        q, r = divmod(len(s), k)
        ans = [''] * q

        for i in range(q):
            ans[i] = s[i*k:(i+1)*k]

        if r > 0:
            ans.append(s[-r:])
            ans[-1] += fill * (k-r)

        return ans
