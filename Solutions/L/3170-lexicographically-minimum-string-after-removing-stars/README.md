**Lexicographically Minimum String After Removing Stars**
=
[Problem Link](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description)

## Intuition
To make the resulting string to be lexicographically smallest, each operation must remove the last smallest 
character. Then we need to store two information, one is a character to compare lexicographical order, and 
the other is an index to choose last smallest character. Thus, min heap is a proper approach.

## Approach
**Step-by-Step Process**

1. While scan `s`, store each character and the corrsponding index to min heap `min_heap`.
    - Since a character is min heap and an index is max heap, store `(char, -idx)`.
  
2. If we meet `*`, then heappop `min_heap` and replace a character corrsponds to `idx` to `*`.

3. Delete every `*`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        min_heap = []

        for idx, char in enumerate(s):
            if char == '*':
                s[-heappop(min_heap)[1]] = '*'

            else:
                heappush(min_heap, (char, -idx))

        return ''.join(s).replace('*', '')
```
