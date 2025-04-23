**Count Largest Group**
=
[Problem Link](https://leetcode.com/problems/count-largest-group/description)

## Intuition
For each integer up to `n`, we need to calculate the sum of digits. As a brute-force approach, simply compute \
every digit sum and store the count as dictionary is possible. Or, it can be solved by DP; a digit sum of `abcd` is 
`a` plus a digit sum of `bcd`, so we can efficiently compute digit sums.

## Approach
**Step-by-Step Process**

1. For each integer `i` up to `n`, extract the quotient and the reminder of `i`, namely `q` and `r`.

2. Clearly `dp[i]` = `dp[q]` + `r`, fill the DP table.

3. Count `digitSum` with `dp[i]`.

4. Count the number of group having the largest size of `digitSum`.
  
## Solutions
```python
# DP - Time Complexity O(n), Space Complexity O(n)
class Solution1:
    def countLargestGroup(self, n: int) -> int:
        dp = [0] * 10**4
        digitSum = [0] * 36

        for i in range(1, n+1):
            q, r = divmod(i, 10)
            dp[i] = dp[q] + r
            digitSum[dp[i]-1] += 1

        return digitSum.count(max(digitSum))


# Brute-force - Time Complexity O(n), Space Complexity O(n)
class Solution2:
    def countLargestGroup(self, n: int) -> int:
        def digitSum(num):
            ans = 0

            while num > 0:
                ans += num % 10
                num = num // 10

            return ans

        
        freq = defaultdict(int)

        for i in range(1, n+1):
            freq[digitSum(i)] += 1

        return len([n for n in freq.keys() if freq[n] == max(freq.values())])
```
