**Count Number of Bad Pairs**
=
[Problem Link](https://leetcode.com/problems/count-number-of-bad-pairs/description)

## Intuition
We focus on 'good pairs', that is, `j - i = nums[j] - nums[i]`, since we can count the number of bad pairs
by substracting good pairs from whole pairs. 
Since the condition also can be written by `nums[i] - i = nums[j] - j`, we track `nums[i] - i`. 
After counting the frequencies of `nums[i] - i`, we calculate total permutation of each values.

## Approach
**Step-by-Step Process**

1. Define `new_nums` which contains `nums[i] - i`.

2. Count the frequency `freq` of values in `new_nums`.

3. For each value of `freq`, a pair can be optained by permutation.
    - With `cnt` frequency, we get `cnt` choose 2 possibilities of pair.
  
4. Sum up every `cnt`, then substract from the total number of permutation.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        new_nums = [nums[i] - i for i in range(n)]

        freq = Counter(new_nums)

        for cnt in freq.values():
            ans += cnt * (cnt-1) // 2

        return (n * (n-1) // 2) - ans
