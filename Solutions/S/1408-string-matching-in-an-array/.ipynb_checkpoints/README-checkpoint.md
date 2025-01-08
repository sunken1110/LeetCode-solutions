**String Matching in an Array**
=
[Problem Link](https://leetcode.com/problems/string-matching-in-an-array/description)

## Intuition
The task is to identify every word which is a substring of the other. This is a simple brute-force search.

## Approach
**Step-by-Step Process**

1. Concatenate every `word` in `words` into 1 `long_word`.
   - To avoid a wrong detection from 'last character + first character' case, we join them with a single blank.
   - **Example** : `["tea", "fast", "eat"]` -> `"tea"` should not be detected as a substring of `"fasteat"

2. Check if `word` is a substring of `long_word`.
   - Note that `word` should be detected at least 2 times, includes `word` itself.
  
## Solutions
```python
# Complexity O(n^2)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        long_word = ' '.join(words)

        for word in words:
            if long_word.count(word) > 1:
                ans.append(word)

        return ans


# Brute-force - Complexity O(n^2)
class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []

        for i in range(n):
            for j in range(n):
                if j != i and words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans
```
