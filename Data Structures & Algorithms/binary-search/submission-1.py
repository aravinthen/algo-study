class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bound1 = 0
        bound2 = len(nums)

        while bound2 != bound1:
            mid = (bound2 + bound1) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                bound2 = mid
            else:
                bound1 = mid + 1
        
        return -1