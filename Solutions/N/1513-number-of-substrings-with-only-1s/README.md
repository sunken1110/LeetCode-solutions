**Number of Substrings With Only 1s**
=
[Problem Link](https://leetcode.com/problems/number-of-substrings-with-only-1s/description)

## Intuition
Scan `s` and find consecutive ones. Use `curr` to count current ones, and add to `ans` which infers the number 
of additional possible substrings with only 1s.

## Approach
**Step-by-Step Process**

1. Initialize the current number of consecutive ones `curr`.

2. For `num` in `s`, count `curr`.
    - The number of possible substrings increases by `curr`.

3. If zero is found, then reset `curr`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        curr = 0
        mod = 10**9 + 7

        for num in s:
            if num == '1':
                curr += 1
                ans += curr

            else:
                curr = 0

        return ans % mod
```
