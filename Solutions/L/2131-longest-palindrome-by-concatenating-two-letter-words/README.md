**Longest Palindrome by Concatenating Two Letter Words**
=
[Problem Link](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description)

## Intuition
We first count the frequency of each word in `words`. To create a palindrome, the candidates of word itself also to be 
a palindrome. If a palindrome of `word` in `words` is also in `words`, then the possible number of concatenation is 
the minimum frequency of two of them. The edge case is that `word` itself is already a palindrome with two same letter. 
This word can be a middle of the palindrome, on the case of at least one of such case has odd frequency, add it as a 
middle of the final palindrome.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count each word's frequency.

2. For each `word` in `words`, check if `words` also contains its palindrome.
    - If so, take the minimum frequency of two corresponding palindromes and count it.
  
3. If `word` itself is already a palindrome, check the parity of frequency.
    - If there exists an odd count, then add it as a middle of the palindrome. This only happens once.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        length = 0
        middle = 0

        for word, val in freq.items():
            pal = word[::-1]

            if pal == word:
                length += (val // 2) * 4

                if val % 2 == 1:
                    middle = 2

            elif pal > word and pal in freq:
                length += min(val, freq[pal]) * 4

        return length + middle
```
