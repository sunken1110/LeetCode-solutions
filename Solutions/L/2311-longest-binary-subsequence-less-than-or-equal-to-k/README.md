**Longest Binary Subsequence Less Than or Equal to K**
=
[Problem Link](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description)

## Intuition
The key point is that we need to use **ALL** zeroes. It is clear for the left-side remaining zeroes, since the 
subsequence is allowed to have leading zeroes. The right-side remaining zeroes are more tricky; for an example 
consider `s=10010` and `k=9` case. First 4 digits subsequence `1001` is already `9`, so it cannot contain additional 
right-side zero. The idea is to delete leading one and to add an additional following zero. This process guarantees 
the result to be always equal or less than the previous subsequence. With this observation, we first take every 
zero and check how many ones can be obtained by converting `k` in binary.

## Approach
**Step-by-Step Process**

1. Initialize `ones` of `s`, and append the indices of ones.

2. Count the number of zeroes in `s`.

3. Convert `k` into binary and count the possible number of ones in `s`.
    - To maintain the order of zeroes and ones, we use `ones`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ones = []

        for idx, num in enumerate(s[::-1]):
            if num == '1':
                ones.append(idx)

        i = 0
        ans = len(s) - len(ones)

        while i < len(ones) and k - 2**ones[i] >= 0:
            k -= 2**ones[i]
            i += 1
            ans += 1

        return ans
```
