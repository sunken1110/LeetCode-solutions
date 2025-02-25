**Number of Sub-arrays With Odd Sum**
=
[Problem Link](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description)

## Intuition
Brute-force requires O(n^2) which is inefficient. To resolve it, we use prefix sum. 
Since `odd + even = odd` only gives odd sum, if ith prefix sum is even then the count of odd sum 
before ith index equals to the odd counts of (i-1)th. Similarly, an even prefix sum corresponds to 
the even counts of (i-1)th.

## Approach
**Step-by-Step Process**

1. Initialize count of odd sums and even sums, `odd_cnt` and `even_cnt`, respectively.
    - **Caution** : `even_cnt` must be initialized as 1, since hidden 0 itself is even.

2. Initialize prefix sum `cum_sum`.

3. Looping in `arr` and apply the counting logic discussed above.
    - If `cum_sum` is even, then `even_cnt += 1` and `cnt += odd_cnt`.
    - If `cum_sum` is odd, then `odd_cnt += 1` and `cnt += even_cnt`.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_cnt = 0
        even_cnt = 1
        cum_sum = 0
        cnt = 0

        for num in arr:
            cum_sum += num

            if cum_sum % 2 == 0:
                even_cnt += 1
                cnt += odd_cnt
            else:
                odd_cnt += 1
                cnt += even_cnt

        return cnt % (10**9 + 7)
```
