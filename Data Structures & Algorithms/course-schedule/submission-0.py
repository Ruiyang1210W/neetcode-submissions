class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)} # map each course to prereq list
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False # detect a loop
            if preMap[course] == []:
                return True # course has no preq
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)
            preMap[course] = []
            return True
    
        for course in range(numCourses):
            if not dfs(course): return False
        return True
