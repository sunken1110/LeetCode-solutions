**Plus One**
=
[Problem Link](https://leetcode.com/problems/plus-one/description)

## Intuition
Simply cover the carry of the least significant bit.

## Approach
**Step-by-Step Process**

1. Check each digit of `digits` in inverse order.
    - If `digit[-1] + 1` occurs a carry, move to the next digit.
    - If not, return `digits` with changed value.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            digits[i] += 1

            if digits[i] < 10:
                return digits

            digits[i] = 0

        return [1] + [0] * n
```
