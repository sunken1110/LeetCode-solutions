**Count Total Number of Colored Cells**
=
[Problem Link](https://leetcode.com/problems/count-total-number-of-colored-cells/description)

## Intuition
This is a simple arithmetic series problem. Each step, the pattern is:

1. 1
2. 1 + 3 + 1
3. 1 + 3 + 5 + 3 + 1

Then the total number of colored cell of nth step is `1 + ... + (2n-3) + (2n-1) + (2n-3) + ... + 1`.

## Approach
**Step-by-Step Process**

1. Compute the nth arithmetic sequence.
  
## Solutions
```python
# Complexity O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1) + 1
