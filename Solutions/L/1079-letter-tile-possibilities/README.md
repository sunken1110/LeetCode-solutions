**Letter Tile Possibilities**
=
[Problem Link](https://leetcode.com/problems/letter-tile-possibilities/description)

## Intuition
To consider which letter can be placed, we build a backtracking DFS. Count each letter in `tiles` 
and put one of them, then backtrack with remained letters.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency `count` of each letters in `tiles`.

2. Put a letter, and then substract the `count`.

3. Since every length of tile is available, `cnt += 1` and backtrack with adjusted `count`.
  
## Solutions
```python
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
```
