**Find the Maximum Length of Valid Subsequence I**
=
[Problem Link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description)

## Intuition
A valid subsequence is one of the following forms; all even / all odd / even-odd alternating. Then we trace the parity 
of each `num` in `nums`, and then count the number of each form. Note that if a current `num` is **even**, 
then the count of alternating previous **odd** must be increased.

## Approach
**Step-by-Step Process**

1. Initialize the count of each valid subsequence.

2. Check the parity of `num` in `nums`, then increase the count of valid subsequence type.

3. Return the maximum length of valid subsequence type.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even = 0
        cnt_odd = 0
        cnt_alt_even = 0
        cnt_alt_odd = 0

        for num in nums:
            if num % 2 == 0:
                cnt_even += 1
                cnt_alt_even = cnt_alt_odd + 1

            else:
                cnt_odd += 1
                cnt_alt_odd = cnt_alt_even + 1

        return max(cnt_even, cnt_odd, cnt_alt_even, cnt_alt_odd)
```
