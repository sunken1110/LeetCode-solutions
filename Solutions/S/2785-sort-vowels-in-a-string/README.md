**Sort Vowels in a String**
=
[Problem Link](https://leetcode.com/problems/sort-vowels-in-a-string/description)

## Intuition
We need two scans of `s`, the first is to find the position of vowels, and the second is to replace vowels 
in non-decreasing order after sorting.

## Approach
**Step-by-Step Process**

1. Scan `s` and append every vowel in `vowels`.

2. Sort `vowels` in non-decreasing order.

3. Again scan `s` and change vowels in sorted order.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def sortVowels(self, s: str) -> str:
        t = list(s)
        vowels = []

        for char in s:
            if char in 'aeiouAEIOU':
                vowels.append(char)

        vowels.sort()
        order = 0
        
        for i in range(len(s)):
            if t[i] in 'aeiouAEIOU':
                t[i] = vowels[order]
                order += 1

        return ''.join(t)
```
