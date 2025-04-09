**Make Lexicographically Smallest Array by Swapping Elements**
=
[Problem Link](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description)

## Intuition
Note that the swap has transitivity, that is, if `nums[i]` and `nums[j]` can be swapped and `nums[j]` and `nums[k]` 
can be swapped, then `nums[i]` and `nums[k]` also can be swapped. The main idea is to divide `nums` into subgroups 
where transitivity holds for each subgroup. Then sort each partition independently and merge it, and finally 
rearrange `nums` into new index order.

## Approach
**Step-by-Step Process**

1. Sort `nums` to divide into partitions.

2. While transitivity holds, append the original index to the partition `sub_idx`.

3. If swap doesn't work, then sort the partition `sub_idx` and append to `sorted_idx`. Initialize `sub_idx`.

4. Rearrange `nums` by indices of `sorted_idx`.

## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        sub_idx = []
        sorted_idx = []
        ans = [0] * len(nums)

        prev = 0
        for val, idx in sorted_nums:
            if val > prev + limit:
                sorted_idx.extend(sorted(sub_idx))
                sub_idx = [idx]

            else:
                sub_idx += [idx]

            prev = val

        sorted_idx.extend(sorted(sub_idx))

        for new_idx, idx in enumerate(sorted_idx):
            ans[idx] = sorted_nums[new_idx][0]

        return ans
```
