#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description

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
