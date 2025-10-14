**Find Resultant Array After Removing Anagrams**
=
[Problem Link](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description)

## Intuition
To check the uniqueness of each anagram, we sort every word in `words` first. Then check if two adjacent words 
are anagrams.

## Approach
**Step-by-Step Process**

1. Sort `word` in `words` to uniquely denote each anagram.

2. Check if two adjacent words are anagram.
    - If not, append to `ans`.
  
## Solutions
```python
# Time Complexity O(mn*log(m)), Space Complexity O(mn)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        anagram = [''.join(sorted(word)) for word in words]
        ans = [words[0]]

        for i in range(len(words)-1):
            if anagram[i] != anagram[i+1]:
                ans.append(words[i+1])

        return ans
```
