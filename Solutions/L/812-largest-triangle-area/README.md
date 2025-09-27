**Largest Triangle Area**
=
[Problem Link](https://leetcode.com/problems/largest-triangle-area/description)

## Intuition
Use Shoelace's formula with brute-force.

## Approach
**Step-by-Step Process**

1. Brute-force for every triplet in `points`.
    - By the Shoelace's formula, the area is `abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))`.
  
## Solutions
```python
# Time Complexity O(n^3), Space Complexity O(1)
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        area = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = max(abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))), area)

        return area
```
