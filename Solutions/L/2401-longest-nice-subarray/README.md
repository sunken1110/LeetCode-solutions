**Longest Nice Subarray**
=
[Problem Link](https://leetcode.com/problems/longest-nice-subarray/description)

## Intuition
Let's consider how a subarray can be **nice**. To be all zero by bitwise AND, there should be no common 
digit. Then, in the cumulative sense, a nice subarray has unique representative that each digit is 
already revealed or not. For example, two bit expressions `1001` and `100` construct `1101`, and if 
the other bit expression holds a nice condition then it doesn't contain 3, 2, and 0th position as 1. 
We use a sliding window technique; cumulatively OR every `num` until the subarray is nice, 
and if the nice condition broken then shrink left window by recovering used bits with XOR.

## Approach
**Step-by-Step Process**

1. Extend right window.

2. If cumulative representative `curr` and `num` of new window cannot be nice, then shrink left window.
    - To recover the shrinked representative, we use XOR.

3. If a shrinked subarray is nice, then extend `num` with OR.

4. Compare the length of `curr` and the maximum length each time an extension finished.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_cnt = 1
        curr = 0

        for right, num in enumerate(nums):
            while left < right and curr & num != 0:
                curr ^= nums[left]
                left += 1

            curr |= num
            max_cnt = max(max_cnt, right - left + 1)

        return max_cnt
```
