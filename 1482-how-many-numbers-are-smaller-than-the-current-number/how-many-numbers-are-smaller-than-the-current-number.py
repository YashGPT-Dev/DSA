class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mallu_mulli = []
        for i in nums:
            count = 0
            for j in range(len(nums)):
                if nums[j] < i:
                    count += 1
            mallu_mulli.append(count)
        return mallu_mulli
