**Maximum Candies Allocated to K Children**
=
[Problem Link](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description)

## Intuition
The problem requires the maximum size of subpile. A naive approach is to sum up the quotient of 
each pile of candies divided by the size of subpile while it is bigger than the number of children. 
For the efficiency, we use a binary search for the size of subpile.

## Approach
**Step-by-Step Process**

1. Initialize the minimum and maximum of size of pile, namely `left` and `right`.

2. Count the maximum number of subpiles that can be allocated equally with `mid` of binary search.
    - If possible, store the size `mid`.

3. Repeat until it is possible to allocate subpiles to at most `k` children. 
  
## Solutions
```python
# Complexity O(n*log(m))
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            cnt = sum(pile // mid for pile in candies)

            if cnt >= k:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans
```
