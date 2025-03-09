**Alternating Groups II**
=
[Problem Link](https://leetcode.com/problems/alternating-groups-ii/description)

## Intuition
To complete the task in 1 loop, we use sliding window technique. The idea is, 
if two adjacent tiles are alternating then `cnt += 1` and if not, initialize `cnt`. Then only the 
alternating groups can have `cnt` larger than or equal to `k`.

## Approach
**Step-by-Step Process**

1. For an easy loop, we extend `colors`.
    - Since we count a size `k` alternating group, the amount is `colors[:k-1]`.

2. Initialize `cnt` and `ans`.
    - **Note** : One tile itself is already alternating, so `cnt` must be initialized to 1.

3. While looping `colors`, check the alternating condition.
    - If two adjacent tiles are different, then `cnt += 1`.
    - If two adjacent coincides, then reset `cnt = 1`.

4. If `cnt >= k`, then count it as an alterating group.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        cnt = 1
        ans = 0

        for i in range(len(colors)-1):
            if colors[i] != colors[i+1]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                ans += 1

        return ans
```
