**Bitwise XOR of All Pairings**
=
[Problem Link](https://leetcode.com/problems/bitwise-xor-of-all-pairings/description)

## Intuition
Key ideas are

1. `xor` by itself is always 0.

2. `xor` operator is commutative, so the operator order doesn't matter.

Suppose `nums2 = [num21, nums22, ... num2n]` and choose one integer `num11` in `nums1`.
Then elements of `nums3` induced by `num11` are `num11 xor num21`, `num11 xor num22`, ..., `num11 xor num2n`.
Therefore, *the bitwise XOR of all integers* in `nums3` induced by `num11` is 
`(num11 xor num11 xor ... xor num11) xor (num21 xor num22 xor ... num2n)` . Here, `xor num11` occurs exactly `len(nums2)` times.
Finally, if we gather every bitwise XOR among `nums1`, `xor num1i` occurs `len(nums2)` times and 
`(num21 xor num22 xor ... num2n)` occurs `len(nums1)` times. Again by the commutativity of `xor`, `xor num2i` occurs exactly
`len(nums1)` times. Therefore, the final result only depends on the parities of `len(nums1)` and `len(nums2)`.


## Approach
**Step-by-Step Process**

1. Check the parities of `len(nums1)` and `len(nums2)`.

2. If `len(nums1)` is odd then calculate `xor`s inside `nums2`, and vice versa.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums1) % 2 != 0:
            for num in nums2:
                ans ^= num

        if len(nums2) % 2 != 0:
            for num in nums1:
                ans ^= num

        return ans
```
