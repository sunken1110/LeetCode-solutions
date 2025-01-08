**Count Prefix and Suffix Pairs I**
=
[Problem Link](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description)

## Intuition
The task is to count a number of words which is both prefix and suffix of the other. This is a simple brute-force search.

## Approach
**Step-by-Step Process**

1. To check the prefix/suffix condition, we use `startswith`/`endswith` method, respectively.
   - **Example** : `["ab", "abcde"]` -> `"abcde".startswith("ab")` returns `True`

2. For each `i`th word in `words`, enough to check the other `(i+1)`th words.
  
## Solutions
```python
# Complexity O(n^2)
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    cnt += 1

        return cnt
```
