**Find Missing and Repeated Values**
=
[Problem Link](https://leetcode.com/problems/find-missing-and-repeated-values/description)

## Intuition
If there was no duplication, then the values are exactly integers from `1` to `n^2`. Note that we can 
compute the total sum of it in O(n), namely `S`. Now suppoase `a` appears twice and `b` is missing. 
Then the total sum of this array is `S + a - b`. Then we can extract both `a` and `b` by subtracting 
every number in grid from `S`; if a specific number appears twice then subtract only once, the result 
will be `S - b` which yields `b` from comparing with `S`.

## Approach
**Step-by-Step Process**

1. Compute the total sum of non-missing array, namely `missing`.
  
2. Initialize `check = set()` to check if an integer appears twice.
  
3. Scan every integer in `grid` and subtract it from `missing`.
    - A repeating can be occurred from `check`.
    - A missing can be occurred from the final value of `missing`.
  
## Solutions
```python
# Complexity O(n^2)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        missing = (n**2) * (n**2 + 1) // 2
        check = set()

        for row in grid:
            for num in row:
                if num not in check:
                    check.add(num)
                    missing -= num

                else:
                    twice = num

        return [twice, missing]
```
