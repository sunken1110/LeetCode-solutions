**Neighboring Bitwise XOR**
=
[Problem Link](https://leetcode.com/problems/neighboring-bitwise-xor/description)

## Intuition
It's an easy application uses the property of `xor`, that `$x \oplus y = z \leftrightarrow x = y \oplus z $`.

## Approach
**Step-by-Step Process**

1. (Solution 1) Sum up every values in `derived`, which is equivalent to the sum of `original`.

2. (Solution 2) Furthermore, since every values are in (0, 1) and added exactly 2 times, `sum(derived)` must be even if `original` exists.
  
## Solutions
```python
# Time Complexity O(n)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = reduce(operator.xor, derived)

        return bool(not ans)

# Time Complexity O(n)
class Solution2:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        return sum(derived) % 2 == 0
```
