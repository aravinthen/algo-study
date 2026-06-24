class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)

        longest = 0
        for i in nums:
            if i-1 not in all_nums:
                current_num = i
                current_longest = 1

                while current_num + 1 in all_nums:
                    current_longest += 1
                    current_num += 1
                
                longest = max(current_longest, longest)
        
        return longest