**Greatest Sum Divisible by Three**
=
[Problem Link](https://leetcode.com/problems/greatest-sum-divisible-by-three/description)

## Intuition
To find the maximum possible sum, we first compute the total sum of `nums`. If the sum itself is already 
divisible by three, then return it. If the remainder is either 1 or 2, we need to subtract minimum sum of 
remainder either 1 or 2. Suppose the remainder is 1, then two cases are possible for the minimum sum; the only 
`num` with remainder 1 is minimum, or sum of two `num`s with remainder 2 is minimum. Similarly we can divide the 
case of remainder of total sum is 2. In conclusion, we update two smallest `num` with modulo 1 and 2, 
respectively, while computing the total sum `total` of `nums`. Up to the remainder of `total`, find the 
minimum removing sum `min_remove` and subtract it from `total`.

## Approach
**Step-by-Step Process**

1. Initialize `total`, `one1`, `one2`, `two1`, and `two2`.
    - `one1` < `one2` are two smallest integers with remainder 1 by modulo 3.
    - `two1` < `two2` are two smallest integers with remainder 2 by modulo 3.

2. In one scan, do the following process.
    - To compute the total sum, add `num` to `total`.
    - Compute the remainder of `num` modulo 3, and then update either `one1`, `one2`, `two1`, or `two2`.

3. Compute the remainder of `total` modulo 3.

4. Up to the result of (3), find the minimal removing sum `min_remove`.
    - If `0`, return `total`.
    - If `1`, either `one1` or `two1` + `two2` is the target.
    - If `2`, either `two1` or `one1` + `one2` is the target.

5. Return `total` - `min_remove`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        one1, one2, two1, two2 = inf, inf, inf, inf
        min_remove = inf

        for num in nums:
            total += num

            if num % 3 == 1:
                if num < one1:
                    one2 = one1
                    one1 = num

                elif num < one2:
                    one2 = num

            elif num % 3 == 2:
                if num < two1:
                    two2 = two1
                    two1 = num

                elif num < two2:
                    two2 = num

        if total % 3 == 0:
            return total

        elif total % 3 == 1:
            if one1 != inf:
                min_remove = min(min_remove, one1)

            if two2 != inf:
                min_remove = min(min_remove, two1 + two2)

        else:
            if two1 != inf:
                min_remove = min(min_remove, two1)

            if one2 != inf:
                min_remove = min(min_remove, one1 + one2)

        return total - min_remove
```
