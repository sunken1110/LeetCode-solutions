**Find All Possible Recipes from Given Supplies**
=
[Problem Link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description)

## Intuition

A naive approach may require a huge amount of search, like recipe-ingredient-recipe-ingredient-... To avoid it, 
we use a memoization while doing DFS which already had maden before. 
Since the order doesn't matter, we consider `supplies` as a set. In each step of DFS, we check 

1. If the recipe is in `supplies`,

2. Or if the recipe is already made in `made`,

3. Or if the required ingredients of recipe exists

If the above 3 conditions are not enough to check whether the recipe is available, we move to next DFS. 
If DFS returns `True`, then memo it and add to `supplies` for an effective search. 

## Approach
**Step-by-Step Process**

1. To check the availability of recipe, we define a dictionary `re2ing` storing required ingredients per each recipe.
  
2. Define DFS with 3 pre-checks which mentioned above.
    - Memoize the result of DFS to `memo` and if the recipe is availble, then add it to `supplies`.
  
3. Return every recipes that can be made.
  
## Solutions
```python
# Complexity O(n+m)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        made = {}
        supplies = set(supplies)
        re2ing = defaultdict(list)

        for recipe, ingredient in zip(recipes, ingredients):
            re2ing[recipe] = ingredient

        
        def dfs(recipe):
            if recipe in supplies:
                return True

            if recipe in made:
                return made[recipe]

            if recipe not in re2ing:
                return False

            made[recipe] = False

            for ingredient in re2ing[recipe]:
                if not dfs(ingredient):
                    return False

            made[recipe] = True
            supplies.add(recipe)

            return True


        return [recipe for recipe in recipes if dfs(recipe)]
```
