**Count Special Triplets**
=
[Problem Link](https://leetcode.com/problems/count-special-triplets/description)

## Intuition
We fix `nums[j]` and count the frequency of `nums[j] * 2` from both left and right side of `nums[j]`. Let 
`l` and `r` be the number of left `nums[j] * 2` and right `nums[j] * 2`, respectively, then the number of special 
triplets with middle `nums[j]` is `l * r`. Each step we move `j` to `j+1`, adjust the counter `lefts` and `rights` 
to finish the process in one pass.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency of both left and right side of fixed index.
    - Initialize `lefts` and `rights` with index 0.
  
2. For each `num` in `nums`, which refers `nums[j]`, adjust `rights` and find `num * 2` from both `lefts` and `rights`.

3. Add `l*r` to `total`, and then adjust the count of `num` in `lefts`.

4. Repeat until we scan every `num` of middle of triplets.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        lefts = Counter()
        rights = Counter(nums)
        total = 0
        mod = 10**9 + 7

        for num in nums:
            rights[num] -= 1
            total = (total + lefts[num*2] * rights[num*2]) % mod
            lefts[num] += 1

        return total
