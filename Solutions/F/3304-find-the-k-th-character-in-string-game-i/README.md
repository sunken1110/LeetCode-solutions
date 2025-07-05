**Find the K-th Character in String Game I**
=
[Problem Link](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description)

## Intuition
Simply generate the converted new word for each step, and then add to the original word. Since the process ends 
when the length of word is at least `k`, we need `ceil(log2(k))` processes.

## Approach
**Step-by-Step Process**

1. Start from the initial word `a`.

2. For each step, convert each letter in word to the next letter and add to the original word.
    - To make a new word to be at least `k` length, repeat the process `ceil(log2(k))` times.
  
3. Return the `k`th letter.
  
## Solutions
```python
# Time Complexity O(log2(k)), Space Complexity O(k)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        for _ in range(ceil(log2(k))):
            new = ''

            for char in word:
                new += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

            word += new

        return word[k-1]
```
