**Find Minimum Operations to Make All Elements Divisible by Three**
=
[Problem Link](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description)

## Intuition
Simply check if each `num` is divisible by three.

## Approach
**Step-by-Step Process**

1. For each `num` in `nums`, compute `num % 3`.
    - If `num` is not divisible, then add 1 operation to `cnt`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        for num in nums:
            if num % 3 != 0:
                cnt += 1

        return cnt
