**Calculate Money in Leetcode Bank**
=
[Problem Link](https://leetcode.com/problems/calculate-money-in-leetcode-bank/description)

## Intuition
Directly compute with mathematical patterns. In a specific week, money increases as an arithmetic sequence. 
Also in a specific day of weeks, money increases as an arithmetic sequence too. Then we use `divmod` to compute 
the number of full weeks and remained days, and can calculate the sum of each arithmetic series.

## Approach
**Step-by-Step Process**

1. Use `divmod` to compute the number of full weeks `w` and remained days `d`.

2. Compute each patterns.
    - Fully saved `w`th week : (1+2+3+4+5+6+7) + `7*w`
    - Total sum of fully saved week : `28*w` + `7*w*(w-1)//2`
    - Remained days : (w+1) + (w+2) + ... + (w+d) = `w*d` + `d*(d+1)//2`
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        w, d = divmod(n, 7)
        
        return 28*w + 7*w*(w-1)//2 + d*(d+1)//2 + w*d
```
