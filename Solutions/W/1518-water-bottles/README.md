**Water Bottles**
=
[Problem Link](https://leetcode.com/problems/water-bottles/description)

## Intuition
Use `divmod` to count new exchanged bottles.

## Approach
**Step-by-Step Process**

1. Set `cnt` as an initial `numBottles`.

2. For each step, compute exchangable bottles with `divmod` and add to `cnt`.

3. Finish the process if the number of remained bottles is less than `numExchange`.

## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles

        while numBottles >= numExchange:
            q, r = divmod(numBottles, numExchange)
            cnt += q
            numBottles = q + r

        return cnt
```
