**First Completely Painted Row or Column**
=
[Problem Link](https://leetcode.com/problems/first-completely-painted-row-or-column/description)

## Intuition
Make a dictionary contains the x, y coordinates of each integer. The main idea is that track the number of 
each row's and column's non-painted blocks until one of them reaches 0. 

## Approach
**Step-by-Step Process**

1. Set a coordinate storing dictionary `visited`. 
  
2. Track the number of each row's and column's non-painted blocks while traversing `arr`.
    - Subtract 1 to corresponding counts of row and column.
    - If one of them reaches 0, then return the index of `arr`. 
  
## Solutions
```python
# Time Complexity O(n*m)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        visited = {mat[row][col]: (row, col) for row in range(rows) 
                    for col in range(cols)}

        row_visited = [cols] * rows
        col_visited = [rows] * cols

        for idx, val in enumerate(arr):
            row, col = visited[val]
            row_visited[row] -= 1
            col_visited[col] -= 1

            if row_visited[row] == 0 or col_visited[col] == 0:
                return idx
```
