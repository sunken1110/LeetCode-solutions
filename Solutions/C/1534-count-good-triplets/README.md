**Count Good Triplets**
=
[Problem Link](https://leetcode.com/problems/count-good-triplets/description)

## Intuition
A simple brute-force works.

## Approach
**Step-by-Step Process**

1. Construct 3 loops for brute-force.
    - To avoid unnecessary search, check `abs(arr[i] - arr[j])` first before entering the last loop.
  
## Solutions
```python
# Time Complexity O(n^3), Space Complexity O(1)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0

        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i]-arr[j]) > a:
                    continue

                for k in range(j+1, len(arr)):
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        cnt += 1

        return cnt
```
