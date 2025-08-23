**Number of Zero-Filled Subarrays**
=
[Problem Link](https://leetcode.com/problems/number-of-zero-filled-subarrays/description)

## Intuition
Subarrays filled with 0 are independent in the sense of block of consecutive zeroes. Then we only need to count the 
number of zeroes in each block, and then count the number of subarrays. Note that the length `n` block contains 
exactly `n*(n+1) / 2` zero-filled subarrays.

## Approach
**Step-by-Step Process**

1. For `num` in `nums`, count the number of consecutive zeroes as `curr`.

2. If nonzero `num` found, then add the number of zero-filled subarrays of previous zero block.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr += 1

            else:
                ans += curr*(curr+1)//2
                curr = 0

        return ans + curr*(curr+1)//2
```
