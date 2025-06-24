#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/sum-of-k-mirror-numbers/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def getPalindrome(num, odd):
            x = num

            if odd:
                x //= 10

            while x > 0:
                num = num * 10 + x % 10
                x //= 10

            return num

        
        def isPalindrome(num, base):
            digits = []

            while num > 0:
                digits.append(num % base)
                num //= base

            return digits == digits[::-1]


        num = 1
        cnt = 0

        while n > 0:
            for i in range(num, num*10):
                if n <= 0:
                    break

                pal = getPalindrome(i, True)

                if isPalindrome(pal, k):
                    cnt += pal
                    n -= 1

            for i in range(num, num*10):
                if n <= 0:
                    break

                pal = getPalindrome(i, False)

                if isPalindrome(pal, k):
                    cnt += pal
                    n -= 1

            num *= 10

        return cnt
