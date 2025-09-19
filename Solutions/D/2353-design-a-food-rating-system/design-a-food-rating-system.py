#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/design-a-food-rating-system/description

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
