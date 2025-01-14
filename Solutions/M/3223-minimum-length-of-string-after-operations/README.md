**Minimum Length of String After Operations**
=
[Problem Link](https://leetcode.com/problems/minimum-length-of-string-after-operations/description)

## Intuition
Key idea is that only one character affects the result per process. If `s[i]` is fixed then we look up both left and
right side of `s[i]`, and if exactly the same characters exist we delete both of them.
That is, for each character in `s`, each process is equivalent to delete 2 of them if the number of that character is more than 3.

## Approach
**Step-by-Step Process**

1. Count the frequency of each character in `s`.
  
2. For each character, count maximum number of processes until the number of it is at most 2.
    - If the frequency is odd, we delete until total number of 1.
    - If the frequency is even, we delete until total number of 2.

3. The length of final string is a sum of the final number of each character.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        
        for char in set('abcdefghijklmnopqrstuvwxyz'):
            cnt = s.count(char)

            if cnt != 0:
                ans += 2 - (cnt % 2) # 1 if odd, 2 if even

        return ans
```
