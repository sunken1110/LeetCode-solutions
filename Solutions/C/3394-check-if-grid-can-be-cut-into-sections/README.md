**Check if Grid can be Cut into Sections**
=
[Problem Link](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description)

## Intuition
We separate x coordinates and y coordinates for check vertical and horizontal cut, respectively. 
First we sort them and check if two adjacent intervals overwrap. If so, then we can't divide them. 
Then merge them as one interval and get the upper bound, and compare to the next interval. 
If there is no overwrap, then we get one possible cut. After checking the overwraps, 
if the total number of possible cuts exceed 2 then we can cut the grid.

## Approach
**Step-by-Step Process**

1. Separate `rectangles` to x coordinates `xcoord` and y coordinates `ycoord`.
    - Since vertical and horizontal cut is algorithmically identical, so we only describe one.

2. To check the overwrap, sort the interval.

3. Initialize the previous upper bound `prev_z2` and count of cuts `cnt`.
    - `cnt = -1` since the lower bound of first interval is not a proper cut. 

4. Define `valid_cut` which searches possible cuts.
    - If so, `cnt += 1`. If `cnt` reach 2, then return True.
    - If not, merge two intervals and find a proper `prev_z2`.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xcoord = []
        ycoord = []

        for x1, y1, x2, y2 in rectangles:
            xcoord.append((x1, x2))
            ycoord.append((y1, y2))


        def valid_cut(coords):
            coords.sort()
            cnt = -1
            prev_z2 = 0

            for z1, z2 in coords:
                if z1 < prev_z2:
                    prev_z2 = max(prev_z2, z2)

                else:
                    cnt += 1
                    
                    if cnt >= 2:
                        return True

                    prev_z2 = z2

            return False
            

        return valid_cut(xcoord) or valid_cut(ycoord)
