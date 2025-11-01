**Count Elements With Maximum Frequency**
=
[Problem Link](https://leetcode.com/problems/count-elements-with-maximum-frequency/description)

## Intuition
Simply use `Counter` to check the frequency of each num in `nums`, then count elements with maximum frequency.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency `freq`.
    - Set the maximum frequency as `max_freq`.
  
2. For each number in `freq`, if the count matches `max_freq` then add to `ans`.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        ans = 0

        for val in freq.values():
            if val == max_freq:
                ans += val

        return ans
