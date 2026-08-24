class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        water = 0
        leftmax, rightmax = height[left], height[right]

        while left < right:
            if leftmax < rightmax:
                left += 1
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    water = water + leftmax - height[left]
            else:
                right -= 1
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water = water + rightmax - height[right]
            
        return water


            