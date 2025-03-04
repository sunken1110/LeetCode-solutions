**Check if Number is a Sum of Powers of Three**
=
[Problem Link](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description)

## Intuition
If the number is a sum of powers of three, then the base 3 conversion will result a digit only consists of 0 and 1. 
Then it is enough to check a remainder divided by 3.

## Approach
**Step-by-Step Process**

1. Compute a remainder of `n` divided by 3.
    - If a remainder is 2, then `n` is not a sum of powers of three. Return False.
    - After checking the least significant bit of `n`, now `n` becomes the quotient of `n` divided by 3.

2. Repeat while `n > 0`, then return True.
  
## Solutions
```python
# Complexity O(m*n)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            digit = n % 3
            if digit == 2:
                return False

            n = n // 3

        return True
```
