#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description

# Time Complexity O(m*log(m) + n*log(n) + k*log(k)), Space Complexity O(m)
# where m = len(tasks), n = len(workers), and k = check of assignable test
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def assignable(n):
            task = deque()
            idx = 0
            num_pills = pills

            for i in range(n):
                while idx < n and tasks[idx] <= workers[i] + strength:
                    task.append(tasks[idx])
                    idx += 1

                if len(task) == 0:
                    return False

                if task[0] <= workers[i]:
                    task.popleft()

                elif num_pills > 0:
                    task.pop()
                    num_pills -= 1

                else:
                    return False

            return True

        
        tasks.sort()
        workers.sort(reverse=True)
        left = 0
        right = min(len(tasks), len(workers))
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if assignable(mid):
                left = mid + 1
                ans = mid

            else:
                right = mid - 1

        return ans
