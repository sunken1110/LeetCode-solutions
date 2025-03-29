**Minimum Moves to Equal Array Elements II**
=
[Problem Link](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description)

## Intuition

Check the below preliminary of this problem, that explains why the median is target uni-value of this grid. 
Also, if an integer can be converted to the target value by add or subtract `x` only, then both remainders of 
an integer and the tarvet value divided by `x` must coincide.
[Preliminary](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description)

## Approach
**Step-by-Step Process**

1. Fix a common remainder `r` with the first element of `grid` divided by `x`.
  
2. Traverse the grid and check if an element has same remainder `r`.
    - If so, then store it into a flatten array `arr`.
    - If not, return -1.

3. Sort `arr` and find the index of median.

4. Compute the total amount of operations and return it.
  
## Solutions
```python
# Time Complexity O(n*log(n))
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        r = grid[0][0] % x
        arr = []

        for row in grid:
            for num in row:
                if r != num % x:
                    return -1

                arr.append(num)

        arr.sort()
        mid = arr[len(arr) // 2]

        return sum([abs(num - mid) for num in arr]) // x
```
