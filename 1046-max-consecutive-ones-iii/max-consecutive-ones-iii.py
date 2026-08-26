class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right=0,0
        max_ones=0
        zero=0
        while right < len(nums):
            if nums[right]==0:
                zero+=1
            if zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            if zero<=k:
                max_ones=max(max_ones,right-left+1)
            right+=1
        return max_ones