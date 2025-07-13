#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description

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
