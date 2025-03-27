**Minimum Moves to Equal Array Elements II**
=
[Problem Link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description)

## Intuition
To minimize the total moves, the target value must be balanced between leftside and rightside. 
Note that ne increment of target value increases 1 moves among the leftside and decreases 1 moves among the rightside. 
Then the difference of number of leftside and rightside elements should be minimized, moreover the target value 
eventually became a median.

## Approach
**Step-by-Step Process**

1. Sort `nums`.
  
2. Find the median `mid` of `nums`.

3. Compute the total movements based on `mid` and return it.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]

        return sum([abs(mid - num) for num in nums])
```
