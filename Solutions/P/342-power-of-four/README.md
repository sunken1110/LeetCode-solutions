**Power of Three**
=
[Problem Link](https://leetcode.com/problems/power-of-four/description)

## Intuition
This is an analogue of the following problem:

[Problem Link](https://leetcode.com/problems/power-of-two/description)

## Approach
**Step-by-Step Process**

1. Divide `n` by 4 until `n > 1`.
    - If a remainder is nonzero, return False.
  
2. Return True.

## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 4 != 0:
                return False

            n //= 4

        return True
```
