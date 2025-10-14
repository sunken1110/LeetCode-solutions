**Container With Most Water**
=
[Problem Link](https://leetcode.com/problems/container-with-most-water/description)

## Intuition
Use two-pointer to shrink the width of container. Compare `left` and `right`, the left and right indices, and 
move the shorter one to the middle.

## Approach
**Step-by-Step Process**

1. Initialize `left` and `right`.

2. While `left` < `right`, shrink the width of container and update the maximum volume of it.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        vol = 0

        while left < right:
            vol = max(vol, (right-left) * min(height[left], height[right]))
        
            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

        return vol
