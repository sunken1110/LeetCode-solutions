**Maximum Fruits Harvested After at Most K Steps**
=
[Problem Link](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description)

## Intuition
Our approach is to use a sliding window technique. The most tricky part is to adjust the width of window, the range 
is decided by the minimum steps to visit all of left and right windows meet `k`. We first set the left `l` as 0 and 
get the location of leftmost fruit as `r`. Get the amount of `fruits[0][0]` (even if we cannot reach this point from 
`startPos`). Expand `l` until the minimum step is in the range of `k`, and substract every amount of intermediate fruit. 
Then move to the next right-side fruit `fruits[1][0]`. Iterate for every fruit and take the maximum value of it.

## Approach
**Step-by-Step Process**

1. Initialize the maximum value `max_val`, the value of current window `val`, and the left index of window `l`.

2. For each `r` in `range(n)`, take the `r`th fruit.

3. Shrink the left-side window `l` until we can visit both `l` and `r` in `k` steps.
    - Substract every intermediate fruit from the `val`.
    - If we find the maximum range, update the maximum value `max_val`.

4. Repeat until we check every fruit as a rightmost fruit.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_val = 0
        val = 0
        l = 0

        for r in range(n):
            val += fruits[r][1]

            while l <= r:
                pos_l = fruits[l][0]
                pos_r = fruits[r][0]
                dist = min(abs(startPos - pos_l) + (pos_r - pos_l),
                            abs(startPos - pos_r) + (pos_r - pos_l))

                if dist > k:
                    val -= fruits[l][1]
                    l += 1

                else:
                    break

            max_val = max(max_val, val)

        return max_val
```
