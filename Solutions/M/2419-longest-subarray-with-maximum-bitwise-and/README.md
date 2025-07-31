**Longest Subarray With Maximum Bitwise AND**
=
[Problem Link](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description)

## Intuition
Among every integer in `nums`, the maximum bitwise AND is nothing but the maximum integer. To see this, suppose 
`n` is the maximum bitwise AND value. If there exists `m > n`, then at least one bit of `m` is 1 and `n` is 0. Then 
`m` itself has already larger maximum bitwise AND value than `n`, so a contradiction occurred. Thus, we only have to 
compute the consecutive length of maximum value of `nums`.

## Approach
**Step-by-Step Process**

1. Find the maximum value `n` of `nums`.

2. Compute the maximum length of consecutive `n`s.
   
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = max(nums)
        max_len = 0
        curr_len = 0
        
        for x in nums:
            if x == n:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 0

        return max_len
```
