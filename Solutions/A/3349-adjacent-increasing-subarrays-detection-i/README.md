**Adjacent Increasing Subarrays Detection I**
=
[Problem Link](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description)

## Intuition
There are 2 cases to get two adjacent subarrays of length `k` that are strictly increasing. One is a subarray of 
length `2*k` is already strictly increasing, and the other is two adjacent length `k` subarrays are strictly 
increasing respectively. To deal with both cases in one pass, we count `l` and `r` which refer the length of 
left and right subarrays that are both strictly increasing. Update `l` and `r` while traversing the indices of 
`nums`. 

## Approach
**Step-by-Step Process**

1. Initialize `l`, `r`, and the previous number `prev`.

2. Scan `nums` in one pass.
    - If current `num` is strictly large than `prev`, then `r += 1`.
    - Else, the previous `r` is now become `l`, and new `r` should be initialized as 1 of `num`.

3. If one of the two valid case occurred, return `True`.
    - One is `l >= k` and `r >= k`.
    - The other is `r >= 2*k`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l, r = 0, 0
        prev = -inf

        for num in nums:
            if num > prev:
                r += 1

            else:
                if (l >= k and r >= k) or (r >= 2*k):
                    return True

                l, r = r, 1
                
            prev = num

        return (l >= k and r >= k) or (r >= 2*k)
```
