**Count Good Triplets in an Array**
=
[Problem Link](https://leetcode.com/problems/count-good-triplets-in-an-array/description)

## Intuition
For triplet `(i, j, k)`, a good triplet holds `nums1[i]`<`nums1[j]`<`nums1[k]` and `nums2[i]`<`nums2[j]`<`nums3[k]`. 
We fix the middle of triplet `j`, and count available left `i` and right `j` within both `nums1` and `nums2`. 
As `j` increases, `left` increases and `right` decreases. Moreover, we need to count the number in specific interval, 
so we adopt a binary indexed tree (BIT) structure for efficient counting.

## Approach
**Step-by-Step Process**

1. Define class `BIT` of binary indexed tree and initialize `bit = BIT(n)`.

2. Define value-index mapping `mapping` of `nums1`.

3. For each `idx`, `num` in `nums2`, count availble `left` and `right`.

4. Available elements of `left` is `bit.query(idx)`.

5. Available elements of `right` is `n-1-idx` - `bit.query(n-1)-left`.
    - `n-1-idx` is a total number of right element in `nums1`.
    - `bit.query(n-1)` is the count of processed element in `nums2`.
    - `bit.query(n-1)-left` is the count of right element in `nums1` which already processed at `nums2` as `left`.

6. Add `left`*`right` to total count.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        class BIT:
            def __init__(self, n):
                self.tree = [0] * (n+1)

            def update(self, idx, x):
                idx += 1
                
                while idx < n+1:
                    self.tree[idx] += x
                    idx += (idx & -idx)

            def query(self, idx):
                idx += 1
                cnt = 0

                while idx > 0:
                    cnt += self.tree[idx]
                    idx -= (idx & -idx)

                return cnt


        n = len(nums1)
        bit = BIT(n)
        cnt = 0
        mapping = {val: idx for idx, val in enumerate(nums1)}

        for num in nums2:
            idx = mapping[num]
            left = bit.query(idx)
            right = (n-1-idx) - (bit.query(n-1)-left)
            cnt += left * right
            bit.update(idx, 1)

        return cnt
