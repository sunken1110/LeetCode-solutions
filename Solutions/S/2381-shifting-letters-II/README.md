**Shifting Letters II**
=
[Problem Link](https://leetcode.com/problems/shifting-letters-ii/description)

## Intuition
The goal is to compute final shifts of each letters in efficient time. We can do by performing brute-force approach,
but this results O(n^2) time complexity. Here, 'prefix sum' is a good technique to apply with.

## Approach
**Step-by-Step Process**

1. Set a `total_shift` array with length `len(s) + 1`, which store indicies of shifts.
   - This array only marks 2 values, start and end indicies, in the sense of prefix sum.

2. Cumulatively sum `total_shift`.

3. Total shift of `s[i]` is the sum of `total_shift[0]` ~ `total_shift[i]`.

4. To deal with the negative index of shift, we use modulus.
  
## Solutions
```python
# Prefix Sum - Complexity O(n)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        total_shift = [0] * (n+1)
        ans = []

        for start, end, direction in shifts:
            total_shift[start] += (1 if direction == 1 else -1)
            total_shift[end + 1] -= (1 if direction == 1 else -1)

        current_shift = 0 # prefix sum
        for i in range(n):
            current_shift += total_shift[i]
            ans.append(chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a')))

        return ''.join(ans)


# Brute-force - Complexity O(n^2)
class Solution2:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shift = [0] * len(s)
        ans = []

        for start, end, direction in shifts:
            for i in range(start, end + 1):
                total_shift[i] += (1 if direction == 1 else -1)

        for i, a in enumerate(s):
            ans.append(chr((ord(a) - ord('a') + total_shift[i]) % 26 + ord('a')))

        return ''.join(ans)
```
