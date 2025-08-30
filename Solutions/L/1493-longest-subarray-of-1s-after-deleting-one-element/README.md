**Longest Subarray of 1's After Deleting One Element**
=
[Problem Link](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description)

## Intuition
Since we only can remove one element, we consider each zero and consecutive ones as one block. Then the 
task transforms to measure the maximum length of two consecutive blocks.

## Approach
**Step-by-Step Process**

1. Initialize the length of first, second block as `prev_len`, `curr_len`, respectively.
    - To deal with the edge case of all ones, we use `check`.

2. If `num` is one, then increase `curr_len` and move to the next number.

3. If `num` is zero, then the block is fixed as previous block and new current block starts.
    - Reset `curr_len` and update `check`.
  
4. For each scanning, update `max_len` as the sum of previous and current length of blocks.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        prev_len = 0
        check = False

        for num in nums:
            if num:
                curr_len +=1

            else:
                prev_len = curr_len
                curr_len = 0
                check = True

            max_len = max(max_len, prev_len + curr_len)

        return max_len if check else len(nums)-1
```
