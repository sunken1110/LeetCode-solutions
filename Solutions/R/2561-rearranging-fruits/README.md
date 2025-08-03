**Rearranging Fruits**
=
[Problem Link](https://leetcode.com/problems/rearranging-fruits/description)

## Intuition
To rearrange fruits, the number of each fruit must be even since both of baskets must have same number of it. 
Also the target fruits are not equally distributed, moreover the number of it is the difference of numbers in 
each basket. Then, the first thing what we do is to check the number of fruit that have to be swapped.

The next task is to swap fruits efficiently. Consider two fruits `i` and `j` that need to be swapped. Since 
the cost is the minimum of `basket1[i]` and `basket2[j]`, we have 2 possible strategies. The first one is 
directly swap `i` and `j`. If `basket1[i] < basket2[j]`, then the cost is `basket1[i]`. The second one is to use 
the minimum cost fruit `k` and swap twice, swap `basket1[i]` with `basket2[k]` and then swap `basket1[k]` and 
`basket2[j]`. This costs `2*basket1[k]`. Thus, we can swap each fruit with the cost of twice of minimum cost and 
the cost of target fruit itself.

## Approach
**Step-by-Step Process**

1. Use `Counter` to check the fruits that need to be swapped and put it in to `swap`.
    - If the number of specific fruit is odd, return -1.

2. Sort `swap` to use more cheaper fruits.

3. Get the minimum cost of swap `min_val`.

4. For each fruit, the cost of swapping is `min(swap[i], 2*min_val)`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter(basket1)

        for x in basket2:
            freq[x] -= 1

        swap = []

        for fruit, cnt in freq.items():
            if cnt % 2 == 1:
                return -1

            diff = abs(cnt // 2)
            swap += [fruit] * diff

        swap.sort()
        min_val = min(basket1 + basket2)
        cost = 0

        for i in range(len(swap) // 2):
            cost += min(swap[i], 2*min_val)

        return cost
```
