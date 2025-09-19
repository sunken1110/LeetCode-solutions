**Design a Food Rating System**
=
[Problem Link](https://leetcode.com/problems/design-a-food-rating-system/description)

## Intuition
Main bottle-neck is to return the highest rated food. To efficiently search the highest rate, we use min-heap 
`food_heap` which stores `(-rating, food)` pair in each cuisine category.

## Approach
**Step-by-Step Process**

1. Initialize `food_info` with a key `food` and a value (`cuisine`, `rating`).

2. To track the heighest rate of each cuisine, initialize `food_heap` as a heap.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n) for Initializing
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.food_heap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            heappush(self.food_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        heappush(self.food_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.food_heap[cuisine]:
            rating, food = self.food_heap[cuisine][0]

            if self.food_info[food] == (cuisine, -rating):
                return food

            heappop(self.food_heap[cuisine])

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```
