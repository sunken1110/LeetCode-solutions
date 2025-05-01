**Count Subarrays Where Max Element Appears at Least K Times**
=
[Problem Link](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description)

## Intuition
First we find the maximum element of `nums`. Also we scan from left to right until the maximum element reveals `k` 
times. Then the target subarrays with a fixed right index can have as its left index the indices before the 1st 
maximum element is found. After finishing count the number of subarrays, move to the right until the next maximum 
element reveals. Now, move left index until the subarrays contain at least `k` maximum elements. Repeat the process.


## Approach
**Step-by-Step Process**

1. Find the maximum element of `nums`, namely `target`.

2. To apply a sliding window technique, increase `right` and count the number of `target` as `check`.
    - Continue until `target` reaches `k`.

3. Increase `left` while `target` is `k`.
    - With fixed `right`, the number of subarrays are exactly `left`.
  
4. Increase `right` again, and repeat the previous process.
    - Until next `target` is found, still the number of possible subarray is `left`.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        left = 0
        check = 0
        cnt = 0

        for right in range(len(nums)):
            if nums[right] == target:
                check += 1

            while check >= k:
                if nums[left] == target:
                    check -= 1

                left += 1

            cnt += left

        return cnt
