**Divisible and Non-divisible Sums Difference**
=
[Problem Link](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description)

## Intuition
We can easily find every `m`-divisible integer less than or equal to `m`. Substracts twice of it from the sum of total 
integer sum.

## Approach
**Step-by-Step Process**

1. Find every `m`-divisible integer.

2. Use O(1) formula of the sum of contiguous integers to compute `num1` and `num2`. 
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num_m = n // m

        return n*(n+1)//2 - m*num_m*(num_m+1)
```
