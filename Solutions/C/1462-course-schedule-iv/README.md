**Course Schedule IV**
=
[Problem Link](https://leetcode.com/problems/course-schedule-iv/description)

## Intuition
For each query `(pre, course)`, we need to check `pre` is a global prerequisite of `course`. We use DFS to traverse 
every chain of prerequisite-course relation. For an efficiency, we store traveled courses in `checked` and 
new chain in `course_pre`. If new chain found, then update it.

## Approach
**Step-by-Step Process**

1. Construct a given map to defaultdict `mapping`.

2. Define DFS which tracks every prerequisite `pre` of `course`.
    - If the `course` is already in `mapping`, then return it.
    - If not, check every prerequisite of `course`.
    - For every prerequisite `pre` of `course`, update the prerequisite of `pre` to `course` with recursive DFS.

3. Call DFS for given queries, and return the answer.
  
## Solutions
```python
# Time Complexity O(n*q), Space Complexity O(n+q)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mapping = defaultdict(list)
        course_pre = defaultdict(set)
        checked = set()

        for pre, course in prerequisites:
            mapping[course].append(pre)

        
        def dfs(course):
            if course in checked:
                return course_pre[course]

            checked.add(course)

            for pre in mapping[course]:
                if pre in course_pre[course]:
                    continue

                course_pre[course].add(pre)
                course_pre[course].update(dfs(pre))

            return course_pre[course]


        for course in range(numCourses):
            dfs(course)

        return [pre in course_pre[course] for pre, course in queries]
