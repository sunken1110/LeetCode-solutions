**Minimize the Maximum Difference of Pairs**
=
[Problem Link](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description)

## Intuition
Since we want to minimize the maximum difference, the binary search is a good approach. Obviously the smaller 
difference occurs by two adjacent elements in ascending or descending order, so we first sort `nums`. The difference 
is 0 when more than two elements are equal and the maximum difference is the difference between the first and the 
last elements. Set them as left and right, and do a binary search. Here, the target of binary search is the 
maximum difference among whole pairs, and we need to count the number of pairs that does not exceed the target. 

## Approach
**Step-by-Step Process**

1. Sort `nums` in ascending order.

2. Initialize `l`, `r` of binary search.
    - `l` = 0.
    - `r` = `nums[-1] - nums[0]`.

3. Do a binary search with the target value `mid = (l+r)//2`.

4. Return `l` of the minimized maximum difference.

## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l+r) // 2
            idx = 0
            cnt = 0

            while idx < n-1:
                if nums[idx+1] - nums[idx] <= mid:
                    cnt += 1
                    idx += 1

                idx += 1

            if cnt >= p:
                r = mid

            else:
                l = mid + 1

        return l
```
