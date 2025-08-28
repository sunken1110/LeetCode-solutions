**Pascal's Triangle**
=
[Problem Link](https://leetcode.com/problems/pascals-triangle/description)

## Intuition
Note that the numbers of `n`th row are same to `n` choose `i` for each `i`.

## Approach
**Step-by-Step Process**

1. For each row, append `n` choose `i`.

## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[] for _ in range(numRows)]

        for i in range(numRows):
            for j in range(i+1):
                pascal[i].append(comb(i, j))

        return pascal
```
