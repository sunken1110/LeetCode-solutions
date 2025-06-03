**Candy**
=
[Problem Link](https://leetcode.com/problems/candy/description)

## Intuition
Since each child must have more candies than their neighbors, we first scan to the right-side direction. For each `i`th child, 
compare to the `i+1`th child. If `i+1`th child has higher rating, then give him one more candy. Since this one scan does 
not guarantee that `i-1`th child may have more candies, so we do one more scan for the left-side direction. If `i-1`th child 
has higher rating than `i`th child and his candies are not enough, then give him one more candy than `i`th child. But if 
`i-1`th child already satisfies the condition of candy, then continue scanning. This can be expressed as a maximum between 
`candies[i+1] + 1` and `candies[i]`.

## Approach
**Step-by-Step Process**

1. Initialize the number of assigned candies `candies`.

2. For the first right direction loop, check the right child's rating.
    - If he has higher rating, then give one more candy.
  
3. For the second left direction loop, check the left child's rating.
    - If he has higher rating, then give `max(candies[i+1] + 1, candies[i])`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1

        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candies[i] = max(candies[i+1] + 1, candies[i])

        return sum(candies)
