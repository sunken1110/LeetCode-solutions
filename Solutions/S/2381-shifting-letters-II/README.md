**Shifting Letters II**
=
[Problem Link](https://leetcode.com/problems/shifting-letters-ii/description)

## Intuition
The goal is to compute final shifts of each letters in efficient time. We can do by performing brute-force approach,
but this results O(n^2) time complexity. Here, 'prefix sum' is a good technique to apply with.

For easy understanding, let's see an example: `s = "abc"`, `shifts = [[0,1,0], [1,2,1], [0,2,1]]`. For `[0,2,1]`, a naive shift table is 
|Index|0|1|2|
|-|-|-|-|
|Shift|1|1|1|

which can be obtained by access **every** index of shifts (0 to 2).

A prefix sum works as follow:
|Index|0|1|2|3|
|-|-|-|-|-|
|Shift|1|0|0|-1|

`"a" (Index[0])` shifts `1 (Shift[0])`, `"b" (Index[1])` shifts `1 (Shift[0] + Shift[1])`, `"c" (Index[2])` shifts
`1 (Shift[0] + Shift[1] + Shift[2])`, and shifts of all the other indices are neutralized by `index 3 (Shift[0] + Shift[1] + Shift[2] + Shift[3])`.
This requires **only** 2 indices (`start`, `end`) to perform each shift.

Back to the example,
|Index|0|1|2|3|
|-|-|-|-|-|
|Shift 1|-1|0|1|0|
|Shift 2|0|1|0|-1|
|Shift 3|1|0|0|-1|
|Total Shift|0|1|1|-2|

`"a"` shifts 0, `"b"` shifts 0 + 1, `"c"` shifts 0 + 1 + 1, so return `"ace"`.

## Approach
**Step-by-Step Process**

1. Set a `total_shift` array with length `len(s) + 1`, which store indices of shifts.
   - This array only marks 2 values, `start` and `end` indices, in the sense of prefix sum.

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
