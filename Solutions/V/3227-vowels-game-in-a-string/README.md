**Vowels Game in a String**
=
[Problem Link](https://leetcode.com/problems/vowels-game-in-a-string/description)

## Intuition
Suppose there are odd number of vowels. Alice play optimally as removing every character of `s`, to make Bob 
has no choice of removing. Now suppose there even number of vowels. Alice again play optimally as removing 
a substring contains odd number of vowels **EXCEPT** the case of no vowel. Then Bob only can remove a substring
contains even number of vowels, so the remaining substring contains odd number of vowels. Next turn, 
Alice can remove whole substring so Alice again can win. Thus, Alice can win if there exists at least one vowel.

## Approach
**Step-by-Step Process**

1. Check if any vowel is in `s`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(char in 'aeiou' for char in s)
```
