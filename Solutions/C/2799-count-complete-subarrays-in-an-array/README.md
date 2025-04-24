**Count Complete Subarrays in an Array**
=
[Problem Link](https://leetcode.com/problems/count-complete-subarrays-in-an-array/description)

## Intuition
Basically, the task it to count the number of subarrays that contain every unique element in `nums`.
Note that if a subarray is complete, then any right-side extension is also complete. Then for a subarray with 
fixed left index `left`, if we can find the minimum right index `right` that makes this subarray complete, 
then the number of complete subarrays with fixed `left` will be automatically decided. With this point of view, 
we use a sliding window technique based on `left`.

## Approach
**Step-by-Step Process**

1. Set the target complete set `distinct` of `nums`

2. For an easy check of completeness of subarray, we use `curr=defaultdict(int)`.

3. Count each element as `right` increases.
   - If the length of `curr` meets `distinct`, then the remaining right-side extensions are also complete. Count it.
   - Then increase `left` and adjust `curr[nums[left]]`.

4. Repeat the above process.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        distinct = set(nums)
        curr = defaultdict(int)
        cnt = 0

        for right in range(n):
            curr[nums[right]] += 1

            while len(curr) == len(distinct):
                cnt += n-right
                curr[nums[left]] -= 1

                if curr[nums[left]] == 0:
                    del curr[nums[left]]

                left += 1

        return cnt
