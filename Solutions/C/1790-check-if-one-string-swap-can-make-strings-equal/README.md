**Check if One String Swap Can Make Strings Equal**
=
[Problem Link](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description)

## Intuition
If two strings can be made equal in one string swap, then they are different at exactly 2 indices. 
Then it is enough to track the number of non-matching indices.

## Approach
**Step-by-Step Process**

1. Check trivial cases.
    - If `s1 == s2`, return `True`.
    - If `s1` and `s2` have different alphabet set, return `False`.

2. Track the non-matching indices with `cnt`.
    - If two corresponding characters are different, `cnt += 1`.
    - If `cnt >= 3` while iterating, return `False`.

3. After iterations, the only cases are `cnt = 1` and `cnt = 2`. Return `True` if `cnt = 2`, else `False`.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        cnt = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1

            if cnt == 3:
                return False

        if cnt == 1:
            return False
        elif cnt == 2:
            return True
