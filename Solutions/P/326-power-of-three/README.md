**Power of Three**
=
[Problem Link](https://leetcode.com/problems/power-of-three/description)

## Intuition
This is an analogue of the following problem:

[Problem Link](https://leetcode.com/problems/power-of-two/description)

## Approach
**Step-by-Step Process**

1. Divide `n` by 3 until `n > 1`.
    - If a remainder is nonzero, return False.
  
2. Return True.

## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 3 != 0:
                return False

            n //= 3

        return True
```
