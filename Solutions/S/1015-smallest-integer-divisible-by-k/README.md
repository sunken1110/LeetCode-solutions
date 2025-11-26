**Smallest Integer Divisible by K**
=
[Problem Link](https://leetcode.com/problems/smallest-integer-divisible-by-k/description)

## Intuition
Note that if such smallest ineger exists, the length of it must be at most `k` by the pigeonhole principle 
in the manner of remainders. To see this, suppose `x1` and `x2` have remainders `r1` and `r2`, respectively, 
in the range of `[0, k-1]`. If `r1` == `r2`, then `x1` - `x2` = `11...11` * `10^i` is divisible by `k`. Then 
there exists another `xk = 11...11` which is also divisible by `k` when `k` is coprime to 2 or 5. Thus, we can
find a target integer if we check at most `k` length integers.


## Approach
**Step-by-Step Process**

1. Initialize current remainder `curr`.

2. Iteratively compute the remainder of next integer `curr * 10 + 1`.
    - If `curr == 0`, return the number of iterations.
  
3. If the number of loops exceed `k`, then return -1.
  
## Solutions
```python
# Time Complexity O(k), Space Complexity O(1)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 0

        for digit in range(1, k+1):
            curr = (curr * 10 + 1) % k

            if curr == 0:
                return digit

        return -1
```
