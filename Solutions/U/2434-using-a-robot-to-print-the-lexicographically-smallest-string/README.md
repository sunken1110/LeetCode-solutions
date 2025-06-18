**Using a Robot to Print the Lexicographically Smallest String**
=
[Problem Link](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description)

## Intuition
To make a new string lexicographically smaller, we need to add faster alphabet first as much as possible, so 
we need to know the occurrence of every alphabet in `s`. Start fomr the smallest alphabet, write every alphabet 
until we reach the last one of it. Store the intermediate not written letters to `stored`. Then a robot has 2 
choices, the one is to go straight to the non-checked next smallest alphabet 'x', and the other is to check 
`stored`. Note that this robot can write `stored` in reverse order. Then if 'x' is smaller than `stored[-1]`, 
a robot should go straight. If not, write letters from `stored` until `stored[-i]` is larger than 'x'. 
Repeat the process until a robot visit every letter of `s`.

## Approach
**Step-by-Step Process**

1. Initialize `p` for the smallest string and `stored` not yet written characters.

2. Scan `s` and store the indices of each character in `pos`.

3. Start from 'a', find the indices in `s` and append it to `p`.
    - Store intermediate characters in `stored`.
    - Update current scanning index `idx`.
  
4. Move to the next alphabet `char`.
    - If `stored[-1]` is smaller than `char`, then append to `p` until `char` is larger.
  
5. Repeat until scanning 'z'.

6. Write remained characters in `stored` reversely.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def robotWithString(self, s: str) -> str:
        pos = defaultdict(list)
        p = []
        stored = []
        prev = -1

        for idx, char in enumerate(s):
            pos[char].append(idx)

        for char in 'abcdefghijklmnopqrstuvwxyz':
            while stored and stored[-1] <= char:
                p.append(stored.pop())

            for idx in pos[char]:
                if idx > prev:
                    p.append(char)
                    stored.extend(s[prev+1:idx])
                    prev = idx

        p += reversed(stored)

        return ''.join(p)
```
