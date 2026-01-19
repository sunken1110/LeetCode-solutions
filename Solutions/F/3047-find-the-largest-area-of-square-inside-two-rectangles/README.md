**Find the Largest Area of Square Inside Two Rectangles**
=
[Problem Link](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description)

## Intuition
Our approach is to use a greedy algorithm. For each `i`th rectangle, get two coordinates of bottom-left and 
top-right to compute the width and the height. Then for each `j`th rectangle with `j>=i`, again get two 
coordinates. Compute the smaller difference to specify the area of the largest square inside them.

## Approach
**Step-by-Step Process**

1. For `i`th rectangle, get `(x1, y1)` and `(x2, y2)` of bottom-left and top-right coordinates.

2. For each `j`th rectangle with `j>=i`, get `(x3, y3)` and `(x4, y4)` to specify the square inside two rectangles.

3. Compute the smaller difference between two coordinates, respectively, which is the width of the largest square.

4. Return the maximum area of them.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        square = 0

        for i in range(n-1):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i+1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                width = min(x2, x4) - max(x1, x3)
                height = min(y2, y4) - max(y1, y3)

                if width > 0 and height > 0 and min(width, height) > square:
                    square = min(width, height)

        return square ** 2
```
