#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description

# Complexity O(n)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        occur = [0] * n
        cnt = 0
        ans = []

        for i in range(n):
            if A[i] == B[i]:
                cnt += 1

            else:
                occur[A[i] - 1] += 1   # Permutation starts from 1 not 0
                occur[B[i] - 1] += 1   # Permutation starts from 1 not 0

                if occur[A[i] - 1] == 2:
                    cnt += 1
                if occur[B[i] - 1] == 2:
                    cnt += 1

            ans.append(cnt)

        return ans
