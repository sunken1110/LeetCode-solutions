**Longest Unequal Adjacent Groups Subsequence I**
=
[Problem Link](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description)

## Intuition
Suppose `words[0]` is contained in a target subsequence. If `words[1]` is in same group, then we pass to `words[2]`. 
To `words[2]` to be contained, it must different both `words[0]` and `words[1]`. The first 2 of the subsequence is then
`[words[0], words[2]]` Now, suppose `words[0]` is passed and `words[1]` is chosen. Similarly, in the sense of `words[2]`, 
the longest subsequence is at most `[words[1], words[2]]`, which is same as `word[0]` contained case. In short, greedy 
algorithm is enough.

## Approach
**Step-by-Step Process**

1. Scan `words` from left to right.

2. If the group of `word[i]` and `word[i+1]` differs, then extend the target subsequence by `word[i+1]`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        ans = []

        for idx, num in enumerate(groups):
            if prev != num:
                ans.append(words[idx])
                prev = num

        return ans
```
