#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set([s])
        ans = s
        queue = [s]

        while queue:
            curr = queue.pop()

            if curr < ans:
                ans = curr

            digits = list(curr)

            for i in range(1, len(digits), 2):
                digits[i] = str((int(digits[i]) + a) % 10)

            op1 = ''.join(digits)

            if op1 not in visited:
                visited.add(op1)
                queue.append(op1)

            op2 = curr[-b:] + curr[:-b]

            if op2 not in visited:
                visited.add(op2)
                queue.append(op2)

        return ans
