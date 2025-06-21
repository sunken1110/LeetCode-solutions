**Maximum Manhattan Distance After K Changes**
=
[Problem Link](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description)

## Intuition
Since north/south moves are independent to east/west moves up to Manhattan distance, we can consider the current 
maximum distance seperately. Also, for each move, Manhattan distance can change at least 2. Then the total range 
of Manhattan distance can be changed at most `min(2*k, move+1)` since the difference cannot exceed the total 
moves.

## Approach
**Step-by-Step Process**

1. Use `defaultdict` to count the moves of each direction.

2. Compute the maximum Manhattan distance for step `idx`.
    - The range is `min(curr_distance + 2*k, move+1)`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = defaultdict(int)
        max_dist = 0

        for idx, move in enumerate(s):
            dirs[move] += 1
            dist = abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W']) + 2*k
            max_dist = max(max_dist, min(dist, idx+1))

        return max_dist
```
