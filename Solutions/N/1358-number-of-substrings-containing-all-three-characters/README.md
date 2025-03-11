**Number of Substrings Containing All Three Characters**
=
[Problem Link](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description)

## Intuition
Suppose a substring contains all three characters, then every longer substring containing it also 
contains all three characters. If we fixed the right-most index of substring, now the problem is to find 
the maximum value of left-most index and this decides a minumal window in the sense of sliding window. 
Check that if the minimal window is of index `i` to `j`, then all of indices `0 <= k <= i` are also 
our targets.

## Approach
**Step-by-Step Process**

1. Initialize the locations of three alphabets with `loc` with -1s.

2. If we meet each alphabet while iteration, mark the index.

3. With the marks, calculate the number of total substrings.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        loc = [-1, -1, -1]
        cnt = 0

        for i in range(n):
            if s[i] == 'a':
                loc[0] = i
            elif s[i] == 'b':
                loc[1] = i
            else:
                loc[2] = i

            cnt += 1 + min(loc)

        return cnt
```
