**Maximum Number of Operations to Move Ones to the End**
=
[Problem Link](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description)

## Intuition
To maximize the number of operations, we need to fill every zeroes. Then, when we meet a zero, we can move 
`prev_ones` of every previous ones. We scan each number of `s`, if a zero is found then add the number of 
previous ones.

## Approach
**Step-by-Step Process**

1. Initialize `prev_ones` and `prev_zeroes`.

2. Check each `num` in `s`.
    - If `num == 0`, trigger `prev_zeroes`.
    - If `num == 1`, process an operation to `prev_ones` ones if `prev_zeroes` is triggered.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        prev_ones = 0
        prev_zeroes = 0


        for num in s:
            if num == '0':
                prev_zeroes = 1

            else:
                ans += prev_ones * prev_zeroes
                prev_ones += 1
                prev_zeroes = 0

        ans += prev_ones * prev_zeroes

        return ans
```
