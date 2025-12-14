**Smallest Number With All Set Bits**
=
[Problem Link](https://leetcode.com/problems/smallest-number-with-all-set-bits/description)

## Intuition
The smallest number with only set bits is of form `2^k - 1`. The task is to find such smallest `k`.

## Approach
**Step-by-Step Process**

1. Find `k` such that `2^k - 1` is the smallest integer grather than or equal to `n`.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**int(log2(n) + 1) - 1
```
