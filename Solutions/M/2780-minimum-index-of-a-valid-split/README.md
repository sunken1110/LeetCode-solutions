**Minimum Index of a Valid Split**
=
[Problem Link](https://leetcode.com/problems/minimum-index-of-a-valid-split/description)

## Intuition
We first find the dominant element and count the number of it. Then split `nums` into two, check if two subarrays 
have the same dominant elements.

## Approach
**Step-by-Step Process**

1. Use `Counter` to find the dominant element `dom_val` and its count `dom_cnt`.

2. Cut `nums` starts from left, and check the counts of `dom_val` of splitted two subarrays.
    - Let `cnt` be the count of `dom_val` in left subarray. Clearly `dom_cnt - cnt` is the count of right subbary. 

3. Find the minimum index that above two counts are dominant, respectively.

## Solutions
```python
# Complexity O(n)
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dom_val, dom_cnt = max(Counter(nums).items(), key=lambda x: x[1])

        cnt = 0
        for i, num in enumerate(nums):
            if num == dom_val:
                cnt += 1

            if cnt > (i+1) // 2 and (dom_cnt - cnt) > (n-i-1) // 2:
                return i

        return -1
```
