**Longest Harmonious Subsequence**
=
[Problem Link](https://leetcode.com/problems/longest-harmonious-subsequence/description)

## Intuition
For a fixed number `num` in `nums`, a harmonious subsequence can contain only `num+1` or `num-1`. Then we need to 
check for each `num`, `num+1` is in `nums` and then count the total number of them. Return the maximum of total 
number.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency `freq` of each `num`.

2. For each `num`, check `num+1` is in `freq`.
    - If so, then take `freq[num]` + `freq[num+1]` as a temporary `max_len`.
  
3. Return the maximum `max_len`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in freq:
            if freq[num+1]:
                max_len = max(max_len, freq[num] + freq[num+1])

        return max_len
```
