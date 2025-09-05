**Find the Number of Ways to Place People II**
=
[Problem Link](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description)

## Intuition
The solution is exactly same to the following problem:

[Problem Link](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description)

## Approach
**Step-by-Step Process**

1. Sort `points` by ascending x-coordiate and descending y-coordinate.

2. For each point in `points`, check if a next point is valid.
    - Initialize the previous y-coordinate as `prev_y`.
    - For every point, if the y-coordinate is in between `prev_y` and y-coordinate of Alice, count +1.
    - If not, there is no any Bob's valid position, so move Alice's position to the next point.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        cnt = 0

        for i in range(n-1):
            x, y = points[i]
            prev_y = -inf

            for j in range(i+1, n):
                if prev_y < points[j][1] <= y:
                    cnt += 1
                    prev_y = points[j][1]

                elif prev_y >= y:
                    break

        return cnt
```
