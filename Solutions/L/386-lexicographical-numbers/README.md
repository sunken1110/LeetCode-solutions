**Lexicographical Numbers**
=
[Problem Link](https://leetcode.com/problems/lexicographical-numbers/description)

## Intuition
Since we need to sort by lexicographial order, DFS approach is a proper solution. Since the smaller integer 
comes first for each digit, if `i`th digit is fixed then the lexicographically next number is an integer with 0 
at `i+1`th digit. We search deeply until the number does not exceed `n`, and then delete the last digit and 
replace the previous digit by +1. Repeat this process until we search `n` distinct element.

## Approach
**Step-by-Step Process**

1. Initialize `ans` as a list.

2. Start from 1, apply DFS approach.
    - For an integer `i`, move to the next digit by `10*i`.
    - If `10*i` exceeds `n`, then just change the last digit by +1.
    - If the last digit is 9 or `i` meets `n`, then remove the last digit.
    - Repeat the above process.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        i = 1

        while len(ans) < n:
            ans.append(i)

            if 10*i <= n:
                i *= 10

            else:
                while i % 10 == 9 or i == n:
                    i //= 10
                
                i += 1

        return ans
```
