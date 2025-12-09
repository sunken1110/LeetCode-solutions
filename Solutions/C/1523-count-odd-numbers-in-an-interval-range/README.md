**Count Odd Numbers in an Interval Range**
=
[Problem Link](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description)

## Intuition
Simply count the number of intermediate odd numbers.

## Approach
**Step-by-Step Process**

1. Return a numeric solution.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1) // 2 - low // 2
