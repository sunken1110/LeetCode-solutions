**Count Good Numbers**
=
[Problem Link](https://leetcode.com/problems/count-good-numbers/description)

## Intuition
This is a simple combinatoric problem. Each even index has 5 choices (0, 2, 4, 6, 8), and each odd index has 4 choices 
(2, 3, 5, 7). Just Compute the total permutation.

## Approach
**Step-by-Step Process**

1. Count the number of even and odd indices, respectively.

2. Compute the total permutation.
  
## Solutions
```python
# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, (n+1)//2, 10**9+7) * pow(4, n//2, 10**9+7)) % (10**9+7)
