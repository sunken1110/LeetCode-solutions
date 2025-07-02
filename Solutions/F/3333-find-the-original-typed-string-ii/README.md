**Find the Original Typed String II**
=
[Problem Link](https://leetcode.com/problems/find-the-original-typed-string-ii/description)

## Intuition
This problem is a more tricky version of the following:

[Problem Link](https://leetcode.com/problems/find-the-original-typed-string-i/description)

When Alice can make several typos, we use dynamic programming to track the current length of possible words. 
First, we define a block that is consist of same letter and count it. Note that for each block we need to pick 
at least one letter. Then construct a 1-D DP array refers to the length of completed word. We only count the word of 
length at most `k-1`, which cannot be a valid case. Also for the efficiency, we use prefix sum to override new 
DP array from the previous block's DP.

## Approach
**Step-by-Step Process**

1. For `word`, count the lengths of each block which is consist of contiguously same letters.

2. If the number of blocks already exceeds `k`, then return the whole permutation.

3. Construct a DP for each block with respect to the possible length of current block's word `max_len`.
    - Use a prefix sum to store the length in range between `length` and `length + max_len`.
  
4. Return the answer from the whole permutation substracts by invalid cases of 3).
  
## Solutions
```python
# Time Complexity O(n+k*m), Space Complexity O(k) where m is a number of consecutive letters
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        blocks = []
        mod = 10**9 + 7
        cnt = 1

        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                cnt += 1

            else:
                blocks.append(cnt)
                cnt = 1

        blocks.append(cnt)
        total = 1

        for max_len in blocks:
            total = (total * max_len) % mod

        if len(blocks) >= k:
            return total

        dp = [0] * k
        dp[0] = 1

        for max_len in blocks:
            dp2 = [0] * k
            pref = 0

            for length in range(1, k):
                pref += dp[length-1]

                if length >= max_len + 1:
                    pref -= dp[length - max_len - 1]

                pref %= mod
                dp2[length] = pref

            dp = dp2

        return (total - sum(dp) % mod) % mod
```
