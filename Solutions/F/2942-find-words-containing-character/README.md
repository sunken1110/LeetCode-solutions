**Find Words Containing Character**
=
[Problem Link](https://leetcode.com/problems/find-words-containing-character/description)

## Intuition
A brute-force approach is enough.

## Approach
**Step-by-Step Process**

1. For each `word` in `words`, if `x` is contained in `word` then append the index of it to `ans`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for idx, word in enumerate(words):
            if x in word:
                ans.append(idx)

        return ans
