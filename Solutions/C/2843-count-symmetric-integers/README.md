**Count Symmetric Integers**
=
[Problem Link](https://leetcode.com/problems/count-symmetric-integers/description)

## Intuition
A naive approach is enough.

## Approach
**Step-by-Step Process**

1. For each number `num` between `low` and `high`, check if it is a palindrome.
    - The length of `num` must be even.
  
## Solutions
```python
# Time Complexity O(n*log(m)) where n = high-low and m is the average length of num, Space Complexity O(1)
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0

        for num in range(low, high+1):
            n = len(str(num))
            
            if n % 2 == 0:
                left = str(num)[:n//2]
                right = str(num)[n//2:]

                if sum(int(i) for i in left) == sum(int(i) for i in right):
                    cnt += 1

        return cnt
