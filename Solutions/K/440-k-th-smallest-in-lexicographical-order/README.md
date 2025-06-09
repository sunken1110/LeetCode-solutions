**K-th Smallest in Lexicographical Order**
=
[Problem Link](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description)

## Intuition
Since there are `n` integers in `[1, n]`, if we sort them by lexicographical order then the first `n/9` integers 
starts from the digit `1`. If we can count the number of integers start with `1`, then we can fix the first digit 
by comparing cumulative counts and `k`. If we fix the first digit, then similarly decide the second digit and so on. 

## Approach
**Step-by-Step Process**

1. Define `count(n, i, j)` that counts the number of integers that starts with `i` and not exceed `j`, and the lexicographical order is less than `n`.

2. For each digit, count the total number of proper integers.

3. By continuing the comparison with cumulative count and `k`, decide digits from left to right.
  
## Solutions
```python
# Complexity O(n*logn))
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(n, i, j):
            cnt = 0

            while i <= n:
                cnt += min(n+1, j) - i
                i *= 10
                j *= 10

            return cnt


        num = 1
        curr_cnt = 1

        while curr_cnt < k:
            cnt = count(n, num, num+1)

            if curr_cnt + cnt <= k:
                curr_cnt += cnt
                num += 1

            else:
                curr_cnt += 1
                num *= 10

        return num
```
