class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegrees[dest] += 1

        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        count = 0
        while q:
            course = q.popleft()
            count += 1

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses
