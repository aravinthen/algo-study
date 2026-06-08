class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diffs:
                return sorted([i, diffs[nums[i]]])
            else:
                diffs[diff] = i