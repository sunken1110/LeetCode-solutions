#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description

# Time Complexity O(n), Space Complexity O(n)
upper = 10**5 + 1
mod = 10**9 + 7
nom = [1] * upper
denom = [1] * upper

for i in range(1, upper):
    nom[i] = i * nom[i-1] % mod
    denom[i] = pow(nom[i], mod-2, mod)


def nCk(n, k):
    return nom[n] * denom[k] * denom[n-k] % mod


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return nCk(n-1, k) * m * pow(m-1, n-k-1, mod) % mod
