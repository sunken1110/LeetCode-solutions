**Count Hills and Valleys in an Array**
=
[Problem Link](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description)

## Intuition
The task is to count the number of inflection points. For each step, compare previous and current integers to check 
if the trend changed. Update the previous integer and move to the next point.

## Approach
**Step-by-Step Process**

1. Set the number of hills and valleys `cnt`, previous trend `diff` and the current trend `curr_diff`.
    - `cnt` is intilized as -1 not to consider the increment or decrement of the first comparison as a changed trend.
  
2. Compare the previous and current integer.
    - If increased then `curr_diff = 1`, or if decreased then `curr_diff = -1`.
  
3. If `curr_diff` is different to previous trend `diff`, then `cnt += 1`.
    - Update `diff` to `curr_diff`.

4. To deal with the edge case of all same integers in `nums`, which is `cnt = -1`, get `max(0, cnt)`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = -1
        prev = nums[0]
        diff = 0
        curr_diff = 0

        for num in nums[1:]:
            if num - prev > 0:
                curr_diff = 1

            elif num - prev < 0:
                curr_diff = -1

            if diff != curr_diff:
                cnt += 1

            diff = curr_diff
            prev = num

        return max(0, cnt)
```
