**Next Greater Numerically Balanced Number**
=
[Problem Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description)

## Intuition
First we define `isBalanced` to check if a given number `num` is balanced. Then find the smallest balanced 
number larger than `n`.

## Approach
**Step-by-Step Process**

1. Define a method `isBalanced` which checks if `num` is a balanced integer.
    - Count the number of each digit in `freq`.
    - If `0` is contained, return False.

2. Find the smallest balanced number larger than `n`.

## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBalanced(num):
            freq = [0] * 10
            
            while num > 0:
                if num % 10 == 0:
                    return False

                freq[num % 10] += 1
                num //= 10

            return all(i == cnt for i, cnt in enumerate(freq) if cnt)


        n += 1

        while not isBalanced(n):
            n += 1

        return n
```
