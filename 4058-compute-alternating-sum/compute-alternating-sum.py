class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        summ=0
        for i in range(len(nums)):
            if i%2==0:
                summ+=nums[i]
            else:
                summ-=nums[i]
        return summ