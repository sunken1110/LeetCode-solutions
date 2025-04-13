#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-count-of-good-integers/description

# Time Complexity O(n * 9**(n/2)), Space Complexity O(1)
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palindrome = []
        half_digit = (n+1)//2
        ans = 0
        
        for num in range(10**(half_digit-1), 10**half_digit):
            half = str(num)
            pal = half + half[::-1] if n % 2 == 0 else half + half[-2::-1]

            if int(pal) % k == 0:
                palindrome.append(pal)

        unique = set()
        
        for pal in palindrome:
            sorted_digits = ''.join(sorted(list(pal)))

            if sorted_digits in unique:
                continue

            unique.add(sorted_digits)

        for pal in unique:
            freq = Counter(pal)
            cnt = factorial(len(pal))

            for val in freq.values():
                cnt //= factorial(val)

            ans += cnt

            if '0' in freq:
                freq['0'] -= 1
                cnt_zero = factorial(len(pal)-1)
                
                for val in freq.values():
                    cnt_zero //= factorial(val)

                ans -= cnt_zero

        return ans
