**Number of Ways to Divide a Long Corridor**
=
[Problem Link](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description)

## Intuition
Since each partition must have exactly two seats, the total number of seats must be even. Then we track 
the number of found seats. Suppose we find first 2 seats, namely a first substring `A`. Again suppose 
there are `num_p` plants between `A` and the remaining substring `B`. (That is, `corridor` = `A` + `P..P` + `B`) 
Then we have exactly `(num_p + 1)` choices to install 1 divider to distribute `P`s and remain `A` as a valid 
section. Thus, our approach is to find two `S` first and then count the intermediate `P`s until the next `S` 
is found. Multiply all `(num_p + 1)` to compute the total number of possibilities.

## Approach
**Step-by-Step Process**

1. Check if `corridor` has positive even number of `S`s.
    - If not, return 0.
  
2. Initialize `num_s`, `num_p`, the number of `S`, `P` in current section, respectively.
    - Increase `num_p` only when current `num_s` is 2.
  
3. If `num_s` is already 2 and the new `S` is found, multiply the possibilities to `cnt`.
    - Reset `num_s` and `num_p`.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2 == 1 or corridor.count('S') == 0:
            return 0

        num_s, num_p = 0, 0
        cnt = 1
        mod = 10**9 + 7

        for w in corridor:
            if w == 'S':
                if num_s == 2:
                    cnt = cnt * (num_p + 1) % mod
                    num_s, num_p = 0, 0

                num_s += 1

            else:
                if num_s == 2:
                    num_p += 1

        return cnt
```
