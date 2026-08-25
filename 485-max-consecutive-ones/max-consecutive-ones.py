class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right=0
        max_ones=0
        while right < len(nums):
            if nums[right]==1:
                max_ones=max(max_ones,right-left+1)
                right+=1
            else:
                right+=1
                left=right  
        return max_ones