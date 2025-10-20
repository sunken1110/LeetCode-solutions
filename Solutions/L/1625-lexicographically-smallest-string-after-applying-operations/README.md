**Lexicographically Smallest String After Applying Operations**
=
[Problem Link](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description)

## Intuition
We use a set of visited string `visited` and BFS to search every valid string after operations. 

## Approach
**Step-by-Step Process**

1. Initialize `visited` and append `s` to `queue` of BFS.

2. Pop one string from `queue` and search two strings after each operation, respectively.
    - If a string is not visited yet, add to `visited` and append to `queue`.
    - Update the smallest string `ans`.
  
3. If every resulted string after operation is visited, return `ans`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set([s])
        ans = s
        queue = [s]

        while queue:
            curr = queue.pop()

            if curr < ans:
                ans = curr

            digits = list(curr)

            for i in range(1, len(digits), 2):
                digits[i] = str((int(digits[i]) + a) % 10)

            op1 = ''.join(digits)

            if op1 not in visited:
                visited.add(op1)
                queue.append(op1)

            op2 = curr[-b:] + curr[:-b]

            if op2 not in visited:
                visited.add(op2)
                queue.append(op2)

        return ans
```
