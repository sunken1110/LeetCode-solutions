**Delete Characters to Make Fancy String**
=
[Problem Link](https://leetcode.com/problems/delete-characters-to-make-fancy-string/description)

## Intuition
Simply trace the count of the consecutive characters. If the count exceeds 2, then skip until a new character is found. 
If not, add it to the fancy string.

## Approach
**Step-by-Step Process**

1. Initialize the previous character `prev` and the count of consecutive characters `cnt`.

2. Scan `s`.
    - If a character is equal to `prev`, then increase `cnt` unless `cnt` is already 2.
    - If a new character is found, then reset `cnt`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ''
        cnt = 0
        ans = ''

        for char in s:
            if char == prev:
                if cnt != 2:
                    ans += char
                    cnt += 1

            else:
                prev = char
                cnt = 1
                ans += char

        return ans
```
