**Solving Questions With Brainpower**
=
[Problem Link](https://leetcode.com/problems/solving-questions-with-brainpower/description)

## Intuition
It's a simple dynamic programming task.

## Approach
**Step-by-Step Process**

1. With Top-down approach, we set `dp = [0] * (n+1)` with reverse indexing.

2. Check the index of subproblem and choose better option between to get point or to skip.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            if i + questions[i][1] + 1 < n:
                dp[i] = max(dp[i+1], questions[i][0] + dp[i+questions[i][1] + 1])

            else:
                dp[i] = max(dp[i+1], questions[i][0])

        return dp[0]
```
