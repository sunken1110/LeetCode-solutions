**Snakes and Ladders**
=
[Problem Link](https://leetcode.com/problems/snakes-and-ladders/description)

## Intuition
Since `board` is labeled in a Boustrophedon style, we first flatten the board to 1-D array. For each move, we can 
meet nothing or a snake or a ladder; if we meet a snake or a ladder, then the current position changes to the linked 
location. Then we can use BFS by handling queue with possible next positions. Due to the snakes or ladders, several 
paths can visit already passed location, so we use `visited` to avoid unnecessary traverse.

## Approach
**Step-by-Step Process**

1. Flatten `board` into 1-D array `flatten`.
    - While flattening, traverse 2 adjacent rows since `board` is a zigzag styled array.  

2. Initialize `visited` and `queue` of the starting point.
    - `visited` also indicates the minimum steps to reach each point.

3. Do a BFS.
    - For each move, check if the next point is already visited.
    - If it is a ladder or a snake, move to the linked position.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatten = [0]* (n*n)

        for i in range(n-1, -1, -2):
            for j in range(n):
                flatten[(n-1-i) * n + j] = board[i][j]

                if i >= 1:
                    flatten[(n-i) * n + (n-1-j)] = board[i-1][j]

        visited = [-1] * (n*n)
        queue = deque([0])
        visited[0] = 0

        while queue:
            pos = queue.popleft()

            if pos == n*n-1:
                return visited[pos]

            max_move = min(6, n*n-1-pos)

            for move in range(1, max_move+1):
                next_pos = pos + move

                if flatten[next_pos] != -1:
                    next_pos = flatten[next_pos] - 1

                if visited[next_pos] != -1:
                    continue

                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)

        return -1
```
