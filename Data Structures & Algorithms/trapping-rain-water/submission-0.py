class Solution:
    def trap(self, height: List[int]) -> int:
        water_at_point = [0 for i in range(len(height))]

        for i in range(len(height)):
            to_left = height[:i]
            to_right = height[i:len(height)]

            max_left = max(to_left) if len(to_left) != 0 else 0
            max_right = max(to_right) if len(to_right) != 0 else 0

            water = min(max_left, max_right) - height[i]
            water_at_point[i] = water if water > 0 else 0

        return sum(water_at_point)