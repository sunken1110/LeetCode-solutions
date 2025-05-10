**Push Dominoes**
=
[Problem Link](https://leetcode.com/problems/push-dominoes/description)

## Intuition
If a domino get a push, then adjacent dominoes in the direction of push also falls. To compute how many contiguous 
dominoes falls, we mark the previous push of both left and right directions. In one scan of `dominoes`, 'R' push is 
simple; if the previous 'R' exists then fall every domino between two as 'R'. More complex part is 'L' push; 
if the previous 'R' exists then fall each leftmost and rightmost domino as 'R' and 'L', respectively, and if the 
previous 'R' does not exist then fall every domino between two as 'L'. Don't forget to sum up the last 'R' pushes.

## Approach
**Step-by-Step Process**

1. Initialize `last_right` and `last_left`.
    - `last_right = -1` implies no right push exists or every right push is processed.
  
2. In one scan, check each status of `dominoes`.
    - For a push of index `idx`, fall dominoes between `last_right`/`last_left` and `idx`.

3. Sum up the remaining 'R' pushes.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = list(dominoes)
        last_right = -1
        last_left = 0

        for idx, char in enumerate(dominoes):
            if char == 'R':
                if last_right != -1:
                    for i in range(last_right, idx):
                        ans[i] = 'R'

                last_right = idx

            elif char == 'L':
                if last_right != -1:
                    l, r = last_right, idx

                    while l < r:
                        ans[l], ans[r] = 'R', 'L'
                        l += 1
                        r -= 1

                    last_right = -1

                else:
                    for i in range(last_left, idx):
                        ans[i] = 'L'

                last_left = idx

        if last_right != -1:
            for i in range(last_right, n):
                ans[i] = 'R'

        return ''.join(ans)
