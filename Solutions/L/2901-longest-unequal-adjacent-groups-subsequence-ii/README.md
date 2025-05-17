**Longest Unequal Adjacent Groups Subsequence II**
=
[Problem Link](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description)

## Intuition
Use DP to track the longest subsequence where each `dp[i]` contains alternating words in `words` with maximum length.
For each `dp[i]`, check if the alternating conditions holds for every index `0 <= j < i`. If so, then compare between 
`len(dp[i])` and `len(dp[j]) + 1`, then take the larger one for `dp[i]`. This is for the substitution of dp with
`dp[i] = dp[j] + [words[i]]`.

For an example of `words = ["bab","dab","cab"]` and `groups = [1,2,2]`, the resulting dp is 
`dp = [['bab'], ['dab'], ['bab', 'cab']]`.

## Approach
**Step-by-Step Process**

1. Define `check(a, b)` which compares two words `a` and `b` and return if the hamming distance is exactly 1.
    - Also have to consider the case of `len(a) != len(b)`.

2. For each `i`, scan every indices `0 <= j < i` and check the alternating conditions.
    - 1. Unequal `groups`.
    - 2. Hamming distance with `check`.
    - 3. Maximum length.

3. Update `dp[i]` with the longest subsequence.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[word] for word in words]


        def check(a, b):
            if len(a) != len(b):
                return False

            diff = 0

            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1

            return diff == 1


        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and check(words[i], words[j]) and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [words[i]]

        return max(dp, key=len)
```
