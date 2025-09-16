**Replace Non-Coprime Numbers in Array**
=
[Problem Link](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description)

## Intuition
Key idea is that for two integers `x` and `y`, `x*y` = `gcd(x, y) * lcm(x, y)`. We check two adjacent numbers in 
`nums` if they are coprime in order. If so, then use gcd method to compute the lcm of them. Replace the left integer 
to computed lcm. Iterate this procedure until we check every number.

## Approach
**Step-by-Step Process**

1. Initialize an index `idx` of newly computed lcm.

2. For each `num` in `nums`, check if the previous number and `num` is coprime.
    - If so, then compute a lcm of them and replace the previous number to the computed lcm.

3. If two adjacent numbers are coprime, then `idx` must be increased by one.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        idx = -1

        for num in nums:
            curr = num

            while idx != -1:
                gcd = math.gcd(nums[idx], curr)

                if gcd == 1:
                    break

                curr = nums[idx] * curr // gcd
                idx -= 1

            idx += 1
            nums[idx] = curr

        return nums[:idx+1]
