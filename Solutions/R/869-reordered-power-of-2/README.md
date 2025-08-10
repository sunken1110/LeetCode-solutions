**Reordered Power of 2**
=
[Problem Link](https://leetcode.com/problems/reordered-power-of-2/description)

## Intuition
Note that if an integer is a reordered power of 2, then the counter of digits are equivalent. Then we only need to 
check if `n` has a same counter of some power of 2 less than 10^9 (~2^30).

## Approach
**Step-by-Step Process**

1. Get the counter of digits of `n`, `digits`.

2. For the power of 2 less than 2^30, compare the counter of it to `digits`.
    - If `digits` is found, then return True.
  
## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(log(n))
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))

        return digits in (sorted(str(1<<x)) for x in range(30))
