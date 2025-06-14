**Maximum Difference by Remapping a Digit**
=
[Problem Link](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description)

## Intuition
The maximum integer can be obtained by replacing the first non-nine digit to nine, and the minimum integer 
can be obtained by replacing the first non-zero digit to zero.

## Approach
**Step-by-Step Process**

1. Initialize `max_num` and `min_num`.

2. Scan `num` and replace digits.
    - Replace the first non-nine digit to nine for `max_num`.
    - Replace the first non-zero digit to zero for `min_num`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        max_num = num
        min_num = num

        for digit in num:
            if digit != '9':
                max_num = num.replace(digit, '9')
                break

        for digit in num:
            if digit != '0':
                min_num = num.replace(digit, '0')
                break

        return int(max_num) - int(min_num)
```
