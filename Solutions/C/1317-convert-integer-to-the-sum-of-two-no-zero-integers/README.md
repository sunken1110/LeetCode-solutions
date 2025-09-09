**Convert Integer to the Sum of Two No-Zero Integers**
=
[Problem Link](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description)

## Intuition
For each `(i, n-i)` pair, check if zero is contained in any one of decimal expression.

## Approach
**Step-by-Step Process**

1. For each `(i, n-i)` pair, check if zero is contained in any one of decimal expression.
    - There always exists at least one such pair.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [str(i), str(n-i)]
```
