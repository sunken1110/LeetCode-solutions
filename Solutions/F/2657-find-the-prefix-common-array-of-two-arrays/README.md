**Find the Prefix Common Array of Two Arrays**
=
[Problem Link](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description)

## Intuition
Permutation of length `n` contains every integers from 1 to n exactly once. Main idea is that a prefix common array of `A` and `B`
returns a count of integers which is already seen among both `A[0]` ~ `A[i]` and `B[0] ~ B[i]`. Thus, for each step, we track the
occurrence of integers until they are found twice.

## Approach
**Step-by-Step Process**

1. Set an occurrence list `occur` and a counter for prefix common `cnt`.
  
2. Traverse `A` and `B` in range `n` to record an occurrence of each integer.
    - If `A[i]` and `B[i]` coincides, then no need to track this integer anymore and `cnt += 1` since a permutation allows each integer only once.
  
3. If `occur[integer]` reaches 2, `cnt += 1`.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        occur = [0] * n
        cnt = 0
        ans = []

        for i in range(n):
            if A[i] == B[i]:
                cnt += 1

            else:
                occur[A[i] - 1] += 1   # Permutation starts from 1 not 0
                occur[B[i] - 1] += 1   # Permutation starts from 1 not 0

                if occur[A[i] - 1] == 2:
                    cnt += 1
                if occur[B[i] - 1] == 2:
                    cnt += 1

            ans.append(cnt)

        return ans
```
