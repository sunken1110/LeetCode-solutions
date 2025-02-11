**Remove All Occurrences of a Substring**
=
[Problem Link](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description)

## Intuition
Use `find` method of string type until there is no substring `part` in `s`.  

## Approach
**Step-by-Step Process**

1. Find the leftmost `part` in `s` by `s.find()`, which returns the leftmost index.

2. Remove a length `len(part)` string starts from the above index.

3. Iterate.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s[:s.find(part)] + s[s.find(part) + len(part):]

        return s
