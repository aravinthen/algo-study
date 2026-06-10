class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        # build prefix
        running = 1
        for n in nums:
            output.append(running)
            running *= n
        
        running = 1
        count = len(nums)-2
        for n in nums[:0:-1]:
            running = n*running
            output[count] *= running
            count -=1

        return output
            