**Maximum Score From Removing Substrings**
=
[Problem Link](https://leetcode.com/problems/maximum-score-from-removing-substrings/description)

## Intuition
The key idea is to remove higher-pointed substring first. For an easy approach, we set the problem which point of 
`ab` is always higher than `ba`. Since a current character is neither 'a' and 'b', then we cannot use the previous 
'a' and 'b' since we only can remove consecutive characters. Then for each 'ab' only block, count the numbers of 
'a' and 'b'. Remove 'ab' first, if there is no more 'ab' then remove remaining 'ba', and move to the next block.
Repeat until every character is checked.

## Approach
**Step-by-Step Process**

1. Initialize the current count of 'a' and 'b', `a` and `b`, respectively, and point `pt`.

2. If `y` > `x`, then reverse `s` and exchange `x` and `y`.

3. For each block, remove `ab` first and add `x`.

4. If every `ab` is removed, then remove remained `ba` and add `y`.
    - The number of remained `ba` is `min(a, b)` since every `ab` is already removed.

5. Move to the next block and reset `a` and `b`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pt = 0
        a = 0
        b = 0
        
        if y > x:
            s = s[::-1]
            y, x = x, y

        for char in s:
            if char == 'a':
                a += 1

            elif char == 'b':
                if a > 0:
                    a -= 1
                    pt += x
                
                else:
                    b += 1

            else:
                pt += y * min(a, b)
                a = 0
                b = 0

        return pt + y * min(a, b)
```
