#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/letter-tile-possibilities/description

# Complexity O(2^n)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        count = Counter(tiles)

        def backtrack(count):
            cnt = 0

            for tile, freq in count.items():
                if freq > 0:
                    cnt += 1 # Add this tile
                    count[tile] -= 1
                        
                    cnt += backtrack(count)

                    count[tile] += 1

            return cnt

        return backtrack(count)
