**Divide Array Into Arrays With Max Difference**
=
[Problem Link](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description)

## Intuition
Since each element in one subarray has difference at most `k`, every subarray is bounded in a range `k`. 
If we sort `nums`, a subarray `nums[3k:3k+3]` must be bounded in a range `k`.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Divide `nums` into `n//3` subarrays by grouping 3 adjacent elements.
    - Check if every subarray is bounded in a range `k`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] <= k:
                ans.append(nums[i:i+3])

            else:
                return []

        return ans
```
