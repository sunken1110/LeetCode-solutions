**Unique Length-3 Palindromic Subsequences**
=
[Problem Link](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description)

## Intuition
The task is to count unique palindromes of length 3, that is, the first and the last character must conincide.
Since we ignore any duplications, if we fix the conciding prefix-suffix pair then the remained work is just to count unique characters
between them.

## Approach
**Step-by-Step Process**

1. For every 26 alphabets, check if prefix-suffix condition hold.

2. Find the indicies of prefix-suffix, then count unique characters in range.
    - `set()` is a proper tool for checking uniqueness.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = 0

        for c in 'abcdefghijklmnopqrstuvwxyz':
            l, r = s.find(c), s.rfind(c)

            if l != -1 and r != -1:
                cnt += len(set(s[l+1:r]))

        return cnt
```
