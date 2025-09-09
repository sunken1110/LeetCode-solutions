**Find N Unique Integers Sum up to Zero**
=
[Problem Link](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description)

## Intuition
Simply take `n-1` integers from `1` to `n-1`, and add the negative sum of them to make a zerosum.

## Approach
**Step-by-Step Process**

1. Take `n-1` integers from `1` to `n-1`.

2. Calculate the negative sum of the above integers, and add it.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, n)] + [-(n-1)*n//2]
```
