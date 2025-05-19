**Sort Colors**
=
[Problem Link](https://leetcode.com/problems/sort-colors/description)

## Intuition
At the first scan, we count the number of each colors. Then at the second scan, we change `nums` in-place by
counted colors starting from 0. If we change every 0, then move to 1 and repeat the same process up to 2.

## Approach
**Step-by-Step Process**

1. Count the number of each colors `mapping`.

2. Change `nums` in order from 0 to 2 using `mapping`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = defaultdict(int)

        for num in nums:
            mapping[num] += 1

        idx = 0

        for color in range(3):
            while mapping[color] > 0:
                nums[idx] = color
                idx += 1
                mapping[color] -= 1
```
