**House Robber IV**
=
[Problem Link](https://leetcode.com/problems/house-robber-iv/description)

## Intuition
The task is to minimize the capability, which is the maximum money the robber stole. Then we can solve 
it with binary search with capability. We set the target capability and count every possible houses while 
skipping the adjacent homes due to the robber's persistence, then compare to `k`.

## Approach
**Step-by-Step Process**

1. Define `check` which returns if the robber can acquire `capability`.
    - If the current house is under `capability`, then stole it and skip the next house.
    - If not, go to the next house.

2. Between `min(nums)` and `max(nums)`, do a binary search.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(capability):
            cnt = 0
            idx = 0

            while idx < len(nums):
                if nums[idx] <= capability:
                    cnt += 1
                    idx += 2

                else:
                    idx += 1

            return cnt >= k

        
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        return left
```
