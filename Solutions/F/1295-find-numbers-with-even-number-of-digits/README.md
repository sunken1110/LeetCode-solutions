**Find Numbers with Even Number of Digits**
=
[Problem Link](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description)

## Intuition
Simply check each `num` in `nums` in order. To efficiently check the number of digits, we use `log10`.

## Approach
**Step-by-Step Process**

1. Use `floor(log10(num)` to check the number of digits, and then sum all up.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(floor(log10(num))) % 2 == 1 for num in nums)
```
