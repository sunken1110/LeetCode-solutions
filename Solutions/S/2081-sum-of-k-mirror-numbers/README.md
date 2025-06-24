**Sum of k-Mirror Numbers**
=
[Problem Link](https://leetcode.com/problems/sum-of-k-mirror-numbers/description)

## Intuition
The main task is to find `n` smallest `k`-mirror numbers, so we start from the generating a palindrome in base-10. 
Note that for a fixed `num`, there are 2 palindromes that can be generated from `num` with odd and even number 
of digits. Then we need to check if a generated base-10 palindrome is also base-k palindrome. The following 
task is to sum first `n` `k`-mirror numbers in order.

## Approach
**Step-by-Step Process**

1. Define `getPalindrome(num, odd: Bool)` to generate a palindrome based on `num`.
    - To generate 2 different palindromes, `odd` is used.
  
2. Define `isPalindrome(num, base)` to check if a generated palindrome is `k`-mirror.

3. For a fixed base of palindrome `i`, find `n` smallest `k`-mirror numbers.

## Solutions
```python
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
```
