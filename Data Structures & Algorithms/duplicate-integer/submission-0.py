class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if not i in count:
                count[i] = 1
            else:
                return True
                
        return False