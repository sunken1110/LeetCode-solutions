**Type of Triangle**
=
[Problem Link](https://leetcode.com/problems/type-of-triangle/description)

## Intuition
Note that the type of triangle can be decide by comparing length of three edges. The key idea is to use the 
inclusion relationship between each types. Equilateral includes isosceles but is not for the opposite, 
and isoceles incudes scalene but also is not for the opposite. We divide each case by checking from the hardest 
condition. For an easy comparison, we sort `nums` first.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Divide cases by checking each condition from the hardest to easiest.
    - First, check if `nums` can consist a triangle.
    - Second, check if it is equilateral.
    - Third, check if it is isosceles.
    - Else, it should be scalene.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return 'none'

        elif nums[0] == nums[1] and nums[1] == nums[2]:
            return 'equilateral'

        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return 'isosceles'

        else:
            return 'scalene'
```
