class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        i=0
        while i < len(nums):
            correctIndex=nums[i]-1
            if nums[correctIndex]!=nums[i]:
                nums[correctIndex],nums[i]=nums[i],nums[correctIndex]
            else:
                i+=1
        for j in range(len(nums)):
            if nums[j]!=j+1:
                mn=j+1
                dp=nums[j]
                return [dp,mn]
        return [-1,-1] 
        