**Construct the Minimum Bitwise Array I**
=
[Problem Link](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description)

## Intuition
Constraints are not tight. For each `num` in `nums`, check every possible `or` computation to make `num`.

## Approach
**Step-by-Step Process**

1. For each `num` in `nums`, check every `i | (i+1)`.
    - If `num` cannot be constructed, add -1 to `ans`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            check = False

            for i in range(num):
                if i | (i+1) == num:
                    ans.append(i)
                    check = True
                    break

            if not check:
                ans.append(-1)

        return ans
