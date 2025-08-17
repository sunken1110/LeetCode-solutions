**Power of Two**
=
[Problem Link](https://leetcode.com/problems/power-of-two/description)

## Intuition
Simply divide `n` by 2 until the quotient is 1. If any remainder is nonzero, then return False.

## Approach
**Step-by-Step Process**

1. Divide `n` by 2 until `n > 1`.
    - If a remainder is nonzero, return False.
  
2. Return True.

## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False

            n //= 2

        return True
```
