class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        max_area = 0
        stack = []

        while i < n:
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = heights[top] * width
                max_area = max(max_area, area)
            
        
        while stack:
            top = stack.pop()
            width = n - stack[-1] - 1 if stack else n
            area = heights[top] * width
            max_area = max(max_area, area)

        return max_area