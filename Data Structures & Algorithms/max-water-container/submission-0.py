class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i1 = 0
        i2 = len(heights) - 1

        current_max = 0

        while i1 < i2:
            water = min(heights[i2], heights[i1])*(i2 - i1)
            if water > current_max:
                current_max = water

            if heights[i2] < heights[i1]:
                i2 -= 1
            else:
                i1 +=1
        
        return current_max

