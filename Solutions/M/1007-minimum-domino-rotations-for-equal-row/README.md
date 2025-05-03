**Minimum Domino Rotations For Equal Row**
=
[Problem Link](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description)

## Intuition
Note that if all dominoes can be aligned by same value after rotations, then every domino must have a same value. 
We first set the candidates of that value from `dominoes[0]`, and define `rotate` that check every other dominoes 
that can be rotated or not. Then we need 2 scans for finding `tops[0]` and `bottoms[0]`.

## Approach
**Step-by-Step Process**

1. Define `rotate` which checks the number of rotations for given target value.

2. For the candidates of target `tops[0]` and `bottoms[0]`, do 2 passes of `rotate`.

3. Return the minimum number of rotations.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:        
        def rotate(val, A, B):
            cnt = 0

            for a, b in zip(A, B):
                if a == val:
                    continue

                elif b == val:
                    cnt += 1

                else:
                    return inf

            return cnt
            

        n = len(tops)
        check = {tops[0], bottoms[0]}
        cnt = inf

        for val in check:
            cnt = min(cnt, rotate(val, tops, bottoms), rotate(val, bottoms, tops))

        return cnt if cnt != inf else -1
```
