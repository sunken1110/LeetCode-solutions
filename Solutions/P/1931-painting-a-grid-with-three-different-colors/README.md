**Painting a Grid With Three Different Colors**
=
[Problem Link](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description)

## Intuition
Consider a valid m x n color grid. Then every row are also a valid color grid, and two adjacent rows have 
no two adjacent cells having the same color. The main idea is to construct the candidate set of valid row with DFS, 
and then for each valid row, find the other valid rows with no two adjacent same colored cells. Finally, we construct 
a DP array to cumulatively count the number of possible grid. Also, we use base-3 for express a row; each 0, 1, and 2 
refer red, green, and blue and two adjacent digit cannot be equal.

## Approach
**Step-by-Step Process**

1. Construct a DFS which gives a valid row and store in `candidates`.
    - Use base-3 to express a row, where each value represents three colors.
  
2. For each `seq` in `candidates`, memo valid adjacent rows in `neighbors[seq]`.

3. To count the number of valid grid, use DP where each depth refers the number of cases to stack `seq` and `neighbor[seq]`.

## Solutions
```python
# Time Complexity O((m+n)*k^2), Space Complexity(O(k^2)) where k is len(num_seq)
class Solution(object):
    def colorTheGrid(self, m, n):
        def dfs(idx, prev_color, seq):
            if idx == m:
                candidates.append(seq)
                
                return

            for color in range(3):
                if color != prev_color:
                    dfs(idx+1, color, seq*3 + color)


        candidates = []
        mod = 10**9 + 7

        dfs(0, -1, 0)
        num_seq = len(candidates)
        neighbors = [[] for _ in range(num_seq)]

        for i, seq1 in enumerate(candidates):
            for j, seq2 in enumerate(candidates):
                x, y = seq1, seq2
                check = True

                for _ in range(m):
                    if x % 3 == y % 3:
                        check = False
                        break

                    x //= 3
                    y //= 3

                if check:
                    neighbors[i].append(j)

        dp = [1] * num_seq

        for _ in range(n-1):
            dp2 = [0] * num_seq

            for i in range(num_seq):
                if dp[i]:
                    for j in neighbors[i]:
                        dp2[j] = (dp2[j] + dp[i]) % mod

            dp = dp2

        return sum(dp) % mod
