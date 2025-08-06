**Fruit Into Baskets**
=
[Problem Link](https://leetcode.com/problems/fruit-into-baskets/description)

## Intuition
Since we can contain only two types of fruit, we can apply a sliding window technique for each basket. Start from the 
leftmost index `l=0` and the rightmost index `r`, expand `r` until the types of fruit is at most 2. If the number 
of types exceed 2, drop the leftmost fruit until the basket fit. For each window, update the maximum number of fruits.

## Approach
**Step-by-Step Process**

1. Initialize `basket` to store the current numbers of each fruit, and the left window `l`.

2. Expand the right window `r` until the number of types does not exceeds 2.
    - Update the maximum number of fruits.
  
3. If the number of types exceeds 2, shrink `l` until the basket holds only 2 types of fruit.

4. Repeat for every right window `r`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        max_cnt = 0

        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            max_cnt = max(max_cnt, r-l+1)

        return max_cnt
```
