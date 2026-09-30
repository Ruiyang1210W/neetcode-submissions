class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = 0
        n = len(heights)
        max_area = 0 

        while i < n:
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = width * heights[top]
                max_area = max(max_area, area)
        

        while stack:
            top = stack.pop()
            width = n - stack[-1] -1 if stack else n
            area = width * heights[top]
            max_area = max(max_area, area)

        return max_area
            