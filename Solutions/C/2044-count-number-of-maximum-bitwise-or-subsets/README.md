**Count Number of Maximum Bitwise-OR Subsets**
=
[Problem Link](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description)

## Intuition
Since we have to count the number of subset which has maximum bitwise OR value, we need to check every subset. 
Clearly the maximum bitwise can be obtained by bitwise OR among every integer in `nums`, so we use recursion 
by taking or skipping each integer `num` for every index.

## Approach
**Step-by-Step Process**

1. Compute the maximum bitwise OR value `max_or`.

2. Use a recursion of either taking or skipping for each `num` in `nums`.
    - After every integer is decided to take or skip, return if the value meets `max_or`.
  
## Solutions
```python
# Time Complexity O(2^n), Space Complexity O(n)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)
        n = len(nums)

        def rec(i, curr):
            if i == n:
                return curr == max_or

            take = rec(i + 1, curr | nums[i])
            skip = rec(i + 1, curr)

            return take + skip

        return rec(0, 0)
