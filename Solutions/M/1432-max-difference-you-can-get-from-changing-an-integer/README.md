**Max Difference You Can Get From Changing an Integer**
=
[Problem Link](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description)

## Intuition
This is a tricky version of the following problem:
[Problem Link](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description)

The only difference is `min_num` can not have a leading zero. Since we replace all occurrence of selected 
integer, the target is the first digit that is neither 0 nor 1.

## Approach
**Step-by-Step Process**

1. Initialize `max_num` and `min_num`.

2. Replace the first non-nine digit to nine for `max_num`.

3. For `min_num`, find the first digit that is not in `['0', '1']`.
    - If the digit was found at the leading digit, then replace to 1.
    - Else, replace to 0.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        max_num = num
        min_num = num

        for digit in num:
            if digit != '9':
                max_num = num.replace(digit, '9')
                break

        for idx, digit in enumerate(num):
            if digit not in ['0', '1']:
                if idx == 0:
                    min_num = num.replace(digit, '1')
                    
                else:
                    min_num = num.replace(digit, '0')

                break

        return int(max_num) - int(min_num)
```
