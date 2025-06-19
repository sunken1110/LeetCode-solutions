**Maximum Difference Between Increasing Elements**
=
[Problem Link](https://leetcode.com/problems/maximum-difference-between-increasing-elements/description)

## Intuition
We scan elements from left to right while computing the difference between current element and currently seen 
minimum elements. If we find a new minimum, then replace it.

## Approach
**Step-by-Step Process**

1. Initialize `max_diff = -1` and `prev_min = nums[0]`.
    - If no positive difference found, return `max_diff`.
  
2. Scan `num` in `numbers[1:]` from left to right, and store the difference between `prev_min`.
    - If new minimum found, then replace `prev_min`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        prev_min = nums[0]

        for num in nums[1:]:
            if num == prev_min:
                continue

            elif num < prev_min:
                prev_min = num

            else:
                max_diff = max(max_diff, num-prev_min)

        return max_diff
```
