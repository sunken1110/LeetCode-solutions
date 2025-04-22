#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-ideal-arrays/description

# Time Complexity O(maxValue*sqrt(maxValue)), Space Complexity O(log(maxValue))
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        ans = 0

        
        def getPrimes(num):
            primes = defaultdict(int)
            p = 2

            while num > 1:
                while num % p == 0:
                    primes[p] += 1
                    num //= p

                p += 1

            return primes


        for i in range(1, maxValue + 1):
            primes = getPrimes(i)
            cnt = 1

            for deg in primes.values():
                cnt *= comb(n-1 + deg, deg)

            ans += cnt

        return ans % mod
