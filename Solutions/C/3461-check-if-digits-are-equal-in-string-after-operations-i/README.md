**Check If Digits Are Equal in String After Operations I**
=
[Problem Link](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description)

## Intuition
Naive approach is enough.

## Approach
**Step-by-Step Process**

1. Compute new `s` with operations until `len(s) == 2`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        n = len(s)

        while n > 2:
            for i in range(n-1):
                s[i] = str((int(s[i]) + int(s[i+1])) % 10)
                
            n -= 1

        return s[0] == s[1]
