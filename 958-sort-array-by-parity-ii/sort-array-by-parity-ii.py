class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left=0
        while left < len(nums):
            if nums[left]%2!=0 and left%2==0:
                i=left
                while nums[i]%2!=0:
                    i+=1
                nums[left],nums[i]=nums[i],nums[left]
            if nums[left]%2==0 and left%2!=0:
                i=left
                while nums[i]%2==0:
                    i+=1
                nums[left],nums[i]=nums[i],nums[left]
            left+=1
        return nums