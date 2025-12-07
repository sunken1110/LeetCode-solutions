**Count Operations to Obtain Zero**
=
[Problem Link](https://leetcode.com/problems/count-operations-to-obtain-zero/description)

## Intuition
Simply the operation refers to an Euclidean algorithm. Then use `divmod` to compute the quotient and the remainder, 
then swap `num1` and `num2` to `num2` and the remainder, respectively, until `num1 // num2 == 0`.

## Approach
**Step-by-Step Process**

1. Use `divmod` to compute the quotient `q` and the remainder `r`.

2. Add `q` to the counter and swap `num1`, `num2` to `num2`, `r`.

3. Repeat the process until no remainder occurs.
  
## Solutions
```python
# Time Complexity O(log(max(num1, num2))), Space Complexity O(1)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0

        while num1 and num2:
            q, r = divmod(num1, num2)
            ans += q
            num1, num2 = num2, r

        return ans
```
