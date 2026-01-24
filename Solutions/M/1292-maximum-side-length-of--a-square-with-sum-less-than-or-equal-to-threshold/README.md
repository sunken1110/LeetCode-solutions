**Maximum Side Length Of a Square with Sum Less than or Equal to Threshold**
=
[Problem Link](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description)

## Intuition
Use 2D prefix sum to efficiently compute every square sums. First, construct `isValid` which checks if at least 
one of squares with side length `k` has a square sum less than `threshhold`. Note that if `k` is valid, then
every square size less than `k` is also valid. The maximum valid `k` can be found by brute force. To compute 
a square sum with 2D prefix sum, suppose `pref[i][j]` is a sum of all elements in the rectangle `(0,0)` to 
`(i, j)`. Then a square sum of size `k` start from `(i, j)` can be computed by `pref[i][j]` - `pref[i-k]` - 
`pref[i][j-k]` + `pref[i-k][j-k]`.

## Approach
**Step-by-Step Process**

1. Initialize a 2D prefix sum `pref` with size `(n+1) x (n+1)`.

2. Define `isValid` to check if any size `k` square has a square sum less than or equal to `threshold`.
    - For size `k` square, a square sum is `pref[i][j]` - `pref[i-k]` - `pref[i][j-k]` + `pref[i-k][j-k]`.

3. Check the smallest `k` that `isValid(k)` is False.
    - Return `k-1`.
  
## Solutions
```python
# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def isValid(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    s = pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k]

                    if s <= threshold:
                        return True

            return False

        
        m, n = len(mat), len(mat[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(m):
            row_sum = 0

            for j in range(n):
                row_sum += mat[i][j]
                pref[i+1][j+1] = pref[i][j+1] + row_sum

        for k in range(1, min(m, n) + 1):
            if isValid(k):
                ans = k

            else:
                break

        return ans
```
