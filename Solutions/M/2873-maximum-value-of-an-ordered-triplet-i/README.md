**Maximum Value of an Ordered Triplet I**
=
[Problem Link](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description)

## Intuition
In short,

1. `i` should be maximized.

2. `j` should be minimized after `i`.

3. `k` should be maximized after `j`.

We store prefix maximal value of `i`, `j`, `k` to find the answer in one scanning.

## Approach
**Step-by-Step Process**

1. Let `max_i` be the prefix maximum of `i`, `max_ij` be the prefix maximum of `i-j`, respectively.

2. The answer is the maximum of prefix `max_ij` * `num`.

3. The maximum of prefix `max_ij` is the maximum of prefix `max_i` - `num`.

4. The maximum of prefix `max_i` is the maximum of prefix `num`.

5. Scan `nums` with prefix maximal values in above order.

## Solutions
```python
# Complexity O(n)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_ij = 0
        max_i = 0

        for num in nums:
            ans = max(ans, max_ij * num)
            max_ij = max(max_ij, max_i-num)
            max_i = max(max_i, num)

        return ans
```
