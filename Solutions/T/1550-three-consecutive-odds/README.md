**Three Consecutive Odds**
=
[Problem Link](https://leetcode.com/problems/three-consecutive-odds/description)

## Intuition
Naive approach is enough; count consecutive odds. If we meet even, then reset the count.

## Approach
**Step-by-Step Process**

1. In one pass, count consecutive odds `cnt`.

2. If `cnt == 3`, return `True`.
    - If we meet any even, then reset `cnt = 0`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0

        for num in arr:
            if num % 2 == 1:
                cnt += 1

            else:
                cnt = 0

            if cnt == 3:
                return True

        return False
```
