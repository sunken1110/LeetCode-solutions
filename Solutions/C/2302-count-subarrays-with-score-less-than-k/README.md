**Count Subarrays With Score Less Than K**
=
[Problem Link](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description)

## Intuition
If a subarray has a score more than or equal to `k`, then any super subarray which containing it also has a score 
more than or equal to `k`. Suppose we traverse `nums` from left to right, then we need to sum every element to 
check the score. If the score is over or equal to `k`, then we need to remove elements from the left side until 
the score is again below `k`. This can be efficiently implemented by using sliding window technique.


## Approach
**Step-by-Step Process**

1. Traverse from the `left` to `right` of `nums`.

2. Store a cumulative sum and check the score.
    - If a score is over or equal to `k`, then shrink the subarray from the left.
  
3. With fixed `right`, count the number of possible subarrays.
    - It should be a contiguous subarray ens with `right`, so totally `right-left+1` subarrays are our target.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        cnt = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr * (right-left+1) >= k:
                curr -= nums[left]
                left += 1

            cnt += right-left+1

        return cnt
```
