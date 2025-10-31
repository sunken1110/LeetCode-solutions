**The Two Sneaky Numbers of Digitville**
=
[Problem Link](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description)

## Intuition
Scan every `num` in `nums` and find two duplications.

## Approach
**Step-by-Step Process**

1. Initialize `unique` to check if a number is already seen.

2. If any duplication is found, append to `ans`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        unique = set()

        for num in nums:
            if num not in unique:
                unique.add(num)

            else:
                ans.append(num)

        return ans
```
