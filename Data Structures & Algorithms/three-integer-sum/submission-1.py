class Solution:
    def twoSum(self, nums: List[int], target) -> List[List[int]]:
        i1 = 0
        i2 = len(nums)-1

        sums = []
        while i1 < i2:
            summand = nums[i1]+nums[i2]
            if summand == -target:
                sums.append(sorted((target, nums[i1], nums[i2])))
                i1 = i1 + 1
                i2 = i2 - 1

            elif summand > -target:
                i2 = i2 - 1
            else:
                i1 = i1 + 1
        
        return sums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        summands = []

        for i, num in enumerate(nums):
            reduced_list = sorted([nums[j] for j in range(len(nums)) if j != i])
            sublist = self.twoSum(reduced_list, num)
            
            for val in sublist:
                if val not in summands:
                    summands.append(val)
        
        return [list(i) for i in summands]