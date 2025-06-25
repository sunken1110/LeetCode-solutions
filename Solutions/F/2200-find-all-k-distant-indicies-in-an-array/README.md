**Find All K-Distant Indicies in an Array**
=
[Problem Link](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description)

## Intuition
We use two-pointer with one scanning. For each `nums[j] == key`, store the current `l` and `r` of 
`k`-distant range and append in between indices to the answer. To avoid any redundant append, update 
the range for each step.

## Approach
**Step-by-Step Process**

1. In one scanning, find `idx` that `nums[idx] == key`.

2. Update the `k`-distant range.
    - Left is at least the previous right, so `l = max(r, idx-k)`.
    - Right is at most the length of `nums`, so `r = max(len(nums), idx+k+1)`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        r = 0

        for idx, num in enumerate(nums):
            if num == key:
                l = max(r, idx-k)
                r = min(len(nums), idx+k+1)

                for i in range(l, r):
                    ans.append(i)

        return ans
```
