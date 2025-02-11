**Find the Number of Distinct Colors Among the Balls**
=
[Problem Link](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description)

## Intuition
We use a hashmap to track ball-color pairs. For each step, we check if the ball in query alreaady exists 
in hashmap, and then replace to new color.

## Approach
**Step-by-Step Process**

1. To check if the ball is already colored before, we define a ball-color dictionary `pair`.

2. To count the current number of colors, we define a `colors = defaultdict(int)`.

3. During iterations of `queries`, we check if the ball already shown.
    - If so, we specify the original color `c0` of it and then reduce the number.
    - Indeed, if this `c0` was the last color, then pop it up from `colors`.
  
4. After iterations, the length of `colors` is the answer.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        pair = {}
        ans = []

        for b, c in queries:
            if b in pair:
                c0 = pair[b]
                colors[c0] -= 1

                if colors[c0] == 0:
                    colors.pop(c0)

            pair[b] = c
            colors[c] += 1

            ans.append(len(colors))

        return ans
