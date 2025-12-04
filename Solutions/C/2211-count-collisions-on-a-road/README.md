**Count Collisions on a Road**
=
[Problem Link](https://leetcode.com/problems/count-collisions-on-a-road/description)

## Intuition
We first remove leftmost 'L's and rightmost 'R's which cannot collide forever. Then we track `prev` as
an amount of previous consecutive cars with 'R' direction. Note that if we met 'S' then `prev` is the
number of collisions, and if we met 'L' then `prev + 1` is the number of collisions.

## Approach
**Step-by-Step Process**

1. Remove leftmost 'L's and rightmost 'R's with `lstrip` and `rstrip`.

2. Update the number consecutive cars with 'R' direction `prev`.
    - If the next car is 'L', exactly one adjacent car occurs 2 collisions and the others occur 1.
    - If the next car is 'R', add 1 to `prev`.
    - If the next car is 'S', every cars occur exactly 1 collision.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        prev = 0
        collision = 0

        for d in directions:
            if d == 'L':
                collision += prev + 1
                prev = 0

            elif d == 'R':
                prev += 1

            else:
                collision += prev
                prev = 0
                
        return collision
```
