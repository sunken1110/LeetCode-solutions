**Binary Prefix Divisible By 5**
=
[Problem Link](https://leetcode.com/problems/binary-prefix-divisible-by-5/description)

## Intuition
For each step, a new number is 2 times of previous number plus new least-significant bit. Track the 
remainder of each number divided by 5.

## Approach
**Step-by-Step Process**

1. Initialize `curr` and compute the 10-digit integer `curr` of current binary representation.

2. Track the remainder of `curr` divided by 5.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0

        for bit in nums:
            curr = (curr * 2 + bit) % 5
            ans.append(curr == 0)

        return ans
```
