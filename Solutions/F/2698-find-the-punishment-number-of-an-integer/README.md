**Find the Punishment Number of an Integer**
=
[Problem Link](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description)

## Intuition
We use divide and conquer algorithm, that is, if `x` can be partitioned into `a`, `b`, `c`, ..., then `x-a` can be 
partitioned into `b`, `c`, ... while `x-a` is positive. 

## Approach
**Step-by-Step Process**

1. Define a divide and conquer algorithm `partition(x, target)`.
    - Since `0 <= n <= 1000`, each partition can have at most 3 digits, so divider must be in `(10, 100, 1000)`.
    - If we divide `x` to `x // div`, then `target` must be decremented by `x % div`.

2. For every integer up to `n`, do `partition` and return the punishment number.
  
## Solutions
```python
# Time Complexity O(n*2^log(x, 10)), Space Complexity O(log(x, 10))
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(x, target):
            if x == target:
                return True

            if x == 0:
                return target == 0

            for div in (10, 100, 1000):
                if partition(x // div, target - x % div):
                    return True

            return False

        ans = 0

        for i in range(1, n+1):
            if partition(i*i, i):
                ans += i*i

        return ans
```
