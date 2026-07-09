class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        water = []

        current_max = 0
        for i in range(n):
            current_max = max(current_max, height[i])
            max_left[i] = current_max
        
        current_max = 0
        for i in range(n-1, -1, -1):
            current_max = max(current_max, height[i])
            max_right[i] = current_max
        
        for i in range(n):
            min_water = min(max_left[i], max_right[i]) - height[i] 
            if min_water > 0:
                water.append(min_water)
        
        return sum(water)
        