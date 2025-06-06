**Lexicographically Smallest Equivalent String**
=
[Problem Link](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description)

## Intuition
We have to group equivalent elements and find the representative, which is the lexicographically smallest 
alphabet. This is a typical union-find problem.

## Approach
**Step-by-Step Process**

1. Construct union-find algorithm.
    - The representative of each union is the lexicographically smallest alphabet.

2. Substitute every letter of `baseStr` to the smallest equivalent letter.
  
## Solutions
```python
# Time Complexity O(m+n), Space Complexity O(n)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        
        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return

            if x > y:
                parent[x] = y

            else:
                parent[y] = x

        
        parent = [*range(26)]

        for c1, c2 in zip(s1, s2):
            i1 = ord(c1) - ord('a')
            i2 = ord(c2) - ord('a')
            union(i1, i2)

        return ''.join(chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr)
```
