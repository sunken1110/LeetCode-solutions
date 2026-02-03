**Construct the Minimum Bitwise Array II**
=
[Problem Link](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description)

## Intuition
Tightened version of the following problem:
[Problem Link](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description)

Note that `ans[i]` and `ans[i+1]` are one odd and one even. That is, `nums[i]` must be odd and not to be `2`. 
Also, `nums[i] + 1` changes `nums[i]` as the rightmost 0 to 1 and all every right-side 1s to 0s. In that case, 
`nums[i] || nums[i]+1` is the result of changing the rightmost 0 of `nums[i]` to 1.

## Approach
**Step-by-Step Process**

1. For each `n` in `nums`, find the position of rightmost 0.
    - If `n == 2`, a valid `ans[i]` does not exist.
    - `n+1` flips the rightmost 0 to 1, and all every right-side 1s to 0s.
    - `(n+1) & -(n+1)` refers the rightmost 0.

2. To recover `ans[i]` from `num`, we need to replace the first right-side 1 of rightmost 0.
    - This is `(n+1) & -(n+1) // 2`
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            if n != 2:
                ans.append(n - ((n+1) & (-n-1)) // 2)

            else:
                ans.append(-1)
                
        return ans
