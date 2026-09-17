class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1]*n

        product = 1
        for j in range(n):
            result[j] = result[j] * product
            product = product * nums[j]
        

        product = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * product
            product = product * nums[i]
        
        return result