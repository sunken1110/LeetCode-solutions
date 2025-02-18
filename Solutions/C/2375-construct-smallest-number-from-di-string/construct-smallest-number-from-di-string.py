#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/construct-smallest-number-from-di-string/description

# Complexity O(n)
class Solution1:
    def smallestNumber(self, pattern: str) -> str:
        stack = ['1']
        seq = ''

        for i in range(len(pattern)):
            if pattern[i] == 'I':
                while stack:
                    seq += stack.pop()

            stack.append(str(i+2))

        while stack:
            seq += stack.pop()

        return seq


# Complexity O(2^n * n) - Backtracking
class Solution2:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        check = set()
        seq = []

        def backtrack(idx):
            if len(seq) == n + 1:
                return seq

            for i in range(1, 10):
                if i in check:
                    continue

                if idx == 0 or (pattern[idx-1] == 'I' and seq[-1] < i) or \
                    (pattern[idx-1] == 'D' and seq[-1] > i):
                    check.add(i)
                    seq.append(i)

                    backtrack(idx + 1)

                    if len(seq) == n + 1:
                        return seq

                    seq.pop()
                    check.remove(i)

        return ''.join(map(str, backtrack(0)))
