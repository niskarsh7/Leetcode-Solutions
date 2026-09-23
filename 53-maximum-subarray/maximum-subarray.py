class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summ=0
        maxx=float('-inf')
        for i in range(len(nums)):
            summ+=nums[i]
            maxx=max(maxx,summ)
            if summ<0:
                summ=0
        return maxx      