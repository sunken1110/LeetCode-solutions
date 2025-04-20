**Count the Number of Fair Pairs**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-fair-pairs/description)

## Intuition
Main idea is to construct a method `count(num)` which count the total number of fair pairs with `lower = 0` and `upper = num`. 
Then the answer can be calculated by `count(upper)` - `count(lower-1)`. For `count`, we sort the array and track two pointers 
`left` and `right`, respectively the lower and the upper boundaries. Shrink the range until every pair is fair.

## Approach
**Step-by-Step Process**

1. Construct `count(num)` which counts the number of fair pairs with upper bound `num`.
    - With two pointers `left` and `right`, shrink the range until every pair is fair.
    - Each count should be checked with a fixed `left`, which exactly are totally `right` - `left`.

2. Conclude with `count(upper)` - `count(lower-1)`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()


        def count(num):
            left = 0
            right = n-1
            cnt = 0

            while left < right:
                if nums[left] + nums[right] <= num:
                    cnt += (right-left)
                    left += 1

                else:
                    right -= 1

            return cnt


        return count(upper)- count(lower-1)
