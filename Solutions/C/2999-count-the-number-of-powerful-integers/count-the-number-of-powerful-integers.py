#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-powerful-integers/description

# Time Complexity O(len(finish)) ~ O(1), Space Complexity O(1)
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num: str):
            if len(num) < len(s):
                return 0

            if len(num) == len(s):
                return 1 if num >= s else 0

            cnt = 0
            prefix_len = len(num) - len(s)

            for i in range(prefix_len):
                digit = int(num[i])
                
                if digit > limit:
                    cnt += (limit+1) ** (prefix_len-i)

                    return cnt

                else:
                    cnt += digit * (limit+1) ** (prefix_len-i-1)

            if num[-len(s):] >= s:
                cnt += 1

            return cnt


        return count(str(finish)) - count(str(start-1))
