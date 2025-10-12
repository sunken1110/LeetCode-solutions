**Pacific Atlantic Water Flow**
=
[Problem Link](https://leetcode.com/problems/pacific-atlantic-water-flow/description)

## Intuition
Notice that the borderlines of Atlantic and Pacific Ocean are clearly the target cells, respectively. Then we can 
trace the higher adjacent cells to find the other target cells. We define a dfs which explores the higher adjacent 
cells start from the borderlines (each ocean has 2 borderlines). The answer is the intersection of target sets of 
Atlantic and Pacific oceans.

## Approach
**Step-by-Step Process**

1. Initialize `pacific` and `atlantic`.

2. Define a DFS.
    - For each cell, check the adjacent cells if the height is higher.
    - Recursively travel whole grid and store the target cells to `visited`.

3. For 4 borderlines, call DFS and fill `pacific` and `atlantic`.

4. Return the intersection of `pacific` and `atlantic`.

## Solutions
```python
# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(x, y, visited):
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[x][y] <= heights[nx][ny]:
                    dfs(nx, ny, visited)


        for x in range(m):
            dfs(x, 0, pacific)
            dfs(x, n-1, atlantic)

        for y in range(n):
            dfs(0, y, pacific)
            dfs(m-1, y, atlantic)


        return list(pacific & atlantic)
```
