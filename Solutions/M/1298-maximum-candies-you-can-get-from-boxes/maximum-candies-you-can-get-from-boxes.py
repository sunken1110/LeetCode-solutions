#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        cnt = 0
        visited = set()
        queue = deque()

        for box in initialBoxes:
            if status[box]:
                queue.appendleft(box)
            
            else:
                queue.append(box)
                
        while queue:
            box = queue.popleft()
            
            if box in visited or status[box] == 0:
                continue

            visited.add(box)
            cnt += candies[box]

            for key in keys[box]:
                status[key] = 1

            for new_box in containedBoxes[box]:
                if status[new_box]:
                    queue.appendleft(new_box)

                else:
                    queue.append(new_box)

        return cnt
