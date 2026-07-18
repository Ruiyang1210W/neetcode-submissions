class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answers = [0]*n # create new empty list
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answers[j] = i-j
            stack.append(i)
        return answers



        