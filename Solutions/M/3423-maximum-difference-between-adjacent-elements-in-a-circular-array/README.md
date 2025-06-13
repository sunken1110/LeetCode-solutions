**Maximum Difference Between Adjacent Elements in a Circular Array**
=
[Problem Link](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description)

## Intuition
We simply compute every absolute differenec between two adjacent elements.

## Approach
**Step-by-Step Process**

1. Initialize `prev` as the first elements.

2. Get `diff` of maximum absolute difference between two adjacent elements starts from `prev`.
    - Replace `prev` to the next element.
  
3. Check the last difference of elements in circular relation.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        prev = nums[0]
        diff = 0

        for num in nums[1:]:
            diff = max(diff, abs(num-prev))
            prev = num

        return max(diff, abs(nums[0]-prev))
```
