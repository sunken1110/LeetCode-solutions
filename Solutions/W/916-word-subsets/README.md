**Word Subsets**
=
[Problem Link](https://leetcode.com/problems/word-subsets/description)

## Intuition
A naive approach is to check if each string in `words1` contains every string in `words2`.

Better approach is to check the frequency of each letter. To be universal, every letter of a word in `words1` must have a frequency
greater than or equal to the max frequency of letters among `words2`.

## Approach
**Step-by-Step Process**

1. Set a frequency dictionary of `words2`. For an each check of multiplicity, we use `Counter` module.
  
2. For each `word` in `words1`, check if a subset condition holds.
    - Compare `Counter(word)` and the above frequency dictionary.
    - If any one of strings in `words2` is not a subset of `word`, universality fails.
  
## Solutions
```python
# Complexity O(n + m)
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = []
        freq = {}
        for word in words2:
            for char, n in Counter(word).items():
                if char not in freq or freq[char] < n:
                    freq[char] = n

        for word in words1:
            cnt = Counter(word)
            subset = True
            for char, n in freq.items():
                if char not in cnt or n > cnt[char]:
                    subset = False
                    break

            if subset:
                universal.append(word)

        return universal
```
