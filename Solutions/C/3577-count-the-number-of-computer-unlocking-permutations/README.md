**Count the Number of Computer Unlocking Permutations**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description)

## Intuition
To decrypt `j`th computer, we need `i` < `j` such that `complexity[i]` < `complexity[j]`. Suppose `complexity[j]` 
is smaller than `complexity[0]`, then to decrypt `j`th computer we need another `k`th computer with 
`complexity[k]` < `complexity[j]`. Again to decrypt `k`th computer, and so on, at least one computer cannot 
be decrypted. Therefore, `complexity[0]` should be the smallest. If `complexity[0]` is the smallest, we can 
decrypt every `i > 0`th computer by the computer `0` so any permutation can be accepted. 

## Approach
**Step-by-Step Process**

1. Check if `complexity[0]` is the smallest among `complexity`.
    - If not, return `0`.

2. Return the number of permutations, which coincides to the `n`th factorial.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        mod = 10**9 + 7

        for i in range(2, n):
            ans = (ans * i) % mod

        return ans
```
