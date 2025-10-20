**Adjacent Increasing Subarrays Detection II**
=
[Problem Link](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description)

## Intuition
This problem is an analogue of the following problem:

[Problem Link](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description)

Check each `num` in `nums` and update the maximum `k` in each step. There are two cases that the one is a subarray of 
length `2*k` is already strictly increasing, and the other is two adjacent length `k` subarrays are strictly 
increasing respectively. Update the current length `curr` and the previous length `prev` of strictly increasing 
subarray, then `k` is the maximum of `min(curr, prev)` and `curr // 2`, which refer two valid cases, respectively.

## Approach
**Step-by-Step Process**

1. Initialize `curr`, `prev`, and `k`.

2. Scan each `num` in `nums`.

3. If `num` still satisfy the strictness, `curr += 1`.

4. If not, update `k` as `max(k, curr // 2, min(curr, prev))`.
    - Update `prev` as `curr`, and then initialize `curr` as 1.
  
5. Return the maximum `k`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1
        prev = 0
        k = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr += 1

            else:
                k = max(k, curr // 2, min(curr, prev))
                prev = curr
                curr = 1

        return max(k, curr // 2, min(curr, prev))
```
