#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/description

# Time Complexity O(s + n^3 * t), Space Complexity O(n^2)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        freq = [0] * 26
        mul = [[0] * 26 for _ in range(26)]
        mod = 10**9 + 7
        
        for char in s:
            freq[ord(char) - ord('a')] += 1

        for i in range(26):
            for num in range(nums[i]):
                mul[i][(i+1+num) % 26] += 1

        
        def matmul(A, B):
            rowA = len(A)
            colA = len(A[0])
            colB = len(B[0])
            mat = [[0] * colB for _ in range(rowA)]

            for i in range(rowA):
                for j in range(colB):
                    tmp = 0
                    for k in range(colA):
                        tmp += A[i][k] * B[k][j] % mod

                    mat[i][j] = tmp

            return mat


        def matexp(A, exp):
            n = len(A)
            mat = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

            while exp > 0:
                if exp & 1:
                    mat = matmul(mat, A)

                A = matmul(A, A)
                exp >>= 1

            return mat


        ans = 0
        freq = matmul([freq], matexp(mul, t))

        return sum(freq[0]) % mod
