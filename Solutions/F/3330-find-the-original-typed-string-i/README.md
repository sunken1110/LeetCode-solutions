**Find the Original Typed String I**
=
[Problem Link](https://leetcode.com/problems/find-the-original-typed-string-i/description)

## Intuition
A typo is the character that contiguously occurs at least 2 times. Then we can check in one scanning, 
if two adjacent characters are equal then the count it as a possible original string.

## Approach
**Step-by-Step Process**

1. Check if two adjacent words are equal.
    - If so, count it as a possible original string.
  
2. Additionally count 1 for the case that `word` is not a typo but the original string.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution1:
    def possibleStringCount(self, word: str) -> int:
        return sum(word[i] == word[i+1] for i in range(len(word)-1)) + 1


# Time Complexity O(n), Space Complexity O(1)
class Solution2:
    def possibleStringCount(self, word: str) -> int:
        prev = ''
        cnt = 0
        curr = 0

        for char in word:
            if prev != char:
                prev = char
                cnt += curr
                curr = 0

            else:
                curr += 1

        return cnt + curr + 1
```
