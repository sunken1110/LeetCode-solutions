**Clear Digits**
=
[Problem Link](https://leetcode.com/problems/clear-digits/description)

## Intuition
First, all digits are removed after operation ended. 
In other word, digit can be considered as a trigger of operation; remove the last non-digit character 
during scanning `s` left to right. For an easy implementation, we use stack.

## Approach
**Step-by-Step Process**

1. Define `ans` as a stack to easily remove the last character.

2. If a character is non-digit, append to a list `ans`. If not, remove the last character.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for char in s:
            if char.isdigit():
                if ans:
                    ans.pop()

            else:
                ans.append(char)

        return ''.join(ans)
