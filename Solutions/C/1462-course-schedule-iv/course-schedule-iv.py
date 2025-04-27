#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/course-schedule-iv/description

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
