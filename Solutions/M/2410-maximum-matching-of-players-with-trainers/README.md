**Maximum Matching of Players With Trainers**
=
[Problem Link](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description)

## Intuition
To occur meetings as many as possible, we have to match a lower player to a lower trainer in descending order. 
Then we need two sortings of `players` and `trainers`, and for each player find the lowest ability trainer. 

## Approach
**Step-by-Step Process**

1. Sort `players` and `trainers`.

2. Start from the lowest ability player, find the lowest ability trainer that can be matched to player.
    - If found, then move to the next higher player.
    - If not found, then return the current count of matches.

   
## Solutions
```python
# Time Complexity O(n*log(n)+m*log(m)), Space Complexity O(1)
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m = len(players)
        n = len(trainers)
        cnt = 0
        i =  0
        j = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1

            if j < n:
                cnt += 1

            i += 1
            j += 1

        return cnt
```
