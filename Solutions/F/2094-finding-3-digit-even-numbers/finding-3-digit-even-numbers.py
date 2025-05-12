#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/finding-3-digit-even-numbers/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = defaultdict(int)
        ans = []
        for i in digits:
            freq[i] += 1


        def backtrack(num, idx):
            if idx == 3:
                ans.append(num)

                return

            for i in range(10):
                if not freq[i] or (idx == 0 and i == 0) or (idx == 2 and i % 2):
                    continue

                freq[i] -= 1
                backtrack(num*10+i, idx+1)
                freq[i] += 1

        
        backtrack(0, 0)

        return ans
