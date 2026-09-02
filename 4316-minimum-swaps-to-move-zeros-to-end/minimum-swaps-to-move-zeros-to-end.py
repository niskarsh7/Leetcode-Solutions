class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        count=0
        while left < right:
            if nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left] 
                left+=1
                right-=1
                count+=1
            elif nums[left]==0 and nums[right]==0:
                right-=1
            else:
                left+=1
        return count                  