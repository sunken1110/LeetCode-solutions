**Minimum Time to Make Rope Colorful**
=
[Problem Link](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description)

## Intuition
We need to remove consecutive same colored balloons. To make the rope colorful in minimum time, we remove 
all of such balloons except the one of maximum required time. We scan `colors` in one pass and store the 
previous color. If a consecutive color block is found, then add `neededTime[i]` for all `i` in that block. 
At the end of the search in one block, subtract the maximum time which is the one should not be removed. 

## Approach
**Step-by-Step Process**

1. Initialize the total and maximum required time to remove in current block `curr_time`, `curr_max`, respectively.

2. For each consecutive color block, update `curr_max` and add `neededTime[i]` to `curr_time`.
    - If the sacnning is finished, then subtract the maximum required time among `neededTime[i]`.
    - Add the minimum time to make current block colorful in `ans`.

3. Repeat the process.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = '-'
        curr_max = 0
        curr_time = 0
        ans = 0

        for i in range(len(colors)):
            if colors[i] == prev:
                curr_max = max(curr_max, neededTime[i])
                curr_time += neededTime[i]

            else:
                ans += curr_time - curr_max
                curr_max = neededTime[i]
                curr_time = neededTime[i]

            prev = colors[i]

        ans += curr_time - curr_max

        return ans
```
