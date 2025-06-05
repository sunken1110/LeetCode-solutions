**Find the Lexicographically Largest String From the Box I**
=
[Problem Link](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description)

## Intuition
We have to split length `len(word)` string to `numFriends` substrings. Since we find the lexicographically 
largest string, always the longer is the better. Also each substring must not to be empty, so the maximum length
of a substring is `len(word) - numFriends + 1`. Thus, the candidates are strings of maximum length and the 
substrings of last 3 letters. (For example of `abcx', 'x' is the lexicographically largest string)

## Approach
**Step-by-Step Process**

1. Return `word` for trivial case `numFriends == 1`.

2. Get the maximum length of substring `max_length`.

3. Check every contiguous substrings of length `max_length`.
    - Last 3 letters also should be considered. 

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        max_length = n - numFriends + 1
        ans = 'a'

        for i in range(n):
            curr = word[i:i+max_length]

            if ans < curr:
                ans = curr
        
        return ans
```
