**Minimum Difference Between Highest and Lowest of K Scores**
=
[Problem Link](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description)

## Intuition
The score with minimum differences among `k` students occurs only when the window of scores are minimized. 
That is, we sort `nums` and compare differences of the maximum and the minimum of each `k`-window.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Compute every differences between two numbers with exactly `k` distance.
    - Return the minimum of it.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = nums[k-1] - nums[0]

        for i in range(1, n-k+1):
            min_diff = min(min_diff, nums[i+k-1]-nums[i])

        return min_diff
```
