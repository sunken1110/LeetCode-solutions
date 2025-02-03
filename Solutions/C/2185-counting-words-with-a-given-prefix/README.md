**Counting Words With a Given Prefix**
=
[Problem Link](https://leetcode.com/problems/counting-words-with-a-given-prefix/description)

## Intuition
The task is to count a number of words which is a prefix of the other. This is a simple brute-force search.

## Approach
**Step-by-Step Process**

1. To check the prefix condition, we use `startswith` method.
    - **Example** : `["ab", "abcde"]` -> `"abcde".startswith("ab")` returns `True`
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        return len([word for word in words if word.startswith(pref)])
```
