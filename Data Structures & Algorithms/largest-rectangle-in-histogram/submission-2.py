class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 前后加 0 哨兵
        heights = [0] + heights + [0]
        stack = [0]  # 初始把前置 0 的下标放进去垫底
        max_area = 0

        for i in range(1, len(heights)):
            # 只要当前柱子比栈顶矮，栈顶柱子就找到了它的右矮墙 i
            while heights[i] < heights[stack[-1]]:
                top = stack.pop()           # 弹出的这根柱子当高
                h = heights[top]
                w = i - stack[-1] - 1       # 右矮墙 i，左矮墙 stack[-1]，中间全包含
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area
            