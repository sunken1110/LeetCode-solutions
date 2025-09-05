**Minimum Operations to Make the Integer Zero**
=
[Problem Link](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description)

## Intuition
The task is to find the sum of power of 2's which meets `sum1` - `k`*`sum2` for some integer `k`. 
Note that we can easily find such power of 2's by a unique bit expression. Then what we need to check is 
for each `k`, use `bit_count()` method to count the number of power of 2's. If the count is at most `k`, then 
this integer can be made in `k` operations. The count should not exactly match to `k`, since one `2^i` is equal 
to two `2^(i-1)` for some i, so extra count can be increased to `k`.

## Approach
**Step-by-Step Process**

1. Set the number of operations as `k`.

2. Subtract `num2` from `num1` while the bit count of result value is at most `k`.

## Solutions
```python
# Time Complexity O(60), Space Complexity O(1)
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1

        while num1 > 0:
            num1 -= num2

            if num1 < k:
                return -1

            if num1.bit_count() <= k:
                return k

            k += 1

        return -1
```
