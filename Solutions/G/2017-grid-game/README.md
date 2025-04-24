**Grid Game**
=
[Problem Link](https://leetcode.com/problems/grid-game/description)

## Intuition
The first robot has `len(grid[0])` choices which implies the location of moving down.
If the route of first robot is fixed then the second robot has exactly 2 choices, namely right->down and down->right, 
because the robot pursues the maximal points. Then what we have to do is to minimize the maximal benefit of these 
2 strategy. Note that right->down strategy only acquires the point of top, and vice versa.

## Approach
**Step-by-Step Process**

1. We track the second robot's 2 strategies by `top_sum` and `bottom_sum`.
  
2. For each `len(grid[0])` stratagies of the first robot, compute the `top_sum` and `bottom_sum`.

3. Minimize `max(top_sum, bottom_sum)`.
  
## Solutions
```python
# Time Complexity O(n)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0][1:])
        bottom_sum = 0
        ans = top_sum

        for i in range(1, len(grid[0])):
            top_sum -= grid[0][i]
            bottom_sum += grid[1][i-1]
            temp = max(top_sum, bottom_sum)

            if temp < ans:
                ans = temp

        return ans
```
