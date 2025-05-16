**Maximum Number of Tasks You Can Assign**
=
[Problem Link](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description)

## Intuition

Suppose `n` tasks can be accomplished. Then if we choose top `n` powerful workers, all of them must do one of the task.
In the sense of the weakest worker, he at least has to do the easiest task from `n` tasks. If he can't then we give him 
a pill and do the hardest task among possible tasks. To construct this algorithm, we first sort both `tasks` and 
`workers` to pick `n` most powerful workers and `n` easiest tasks. Then use `deque` structure to deal with possible 
tasks among workers from weaker to stronger. If a worker does not need a pill then `popleft()`which implies the easiest 
task (actually, the order doesn't matter here), or if he need a pill then `pop()` which implies the hardest task he can.

## Approach
**Step-by-Step Process**

1. Sort `tasks` in Ascending order and `workers` in descending order.

2. Define `assignable(n)` which checks if `n` tasks can be assigned.
    - From the weakest worker, choose feasible tasks with pill.
    - If the worker can do a task from the candidates without pill, then assign it.
    - If not, give a pill and assign the hardest work.
    - If you can assign every `n` tasks with limited pill, return True.

3. For the candidates `n` of maximum task, do a binary search.
  
## Solutions
```python
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
```
