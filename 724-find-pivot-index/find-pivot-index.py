class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        summ=sum(nums[:])
        left=0
        right=0
        for i in range(len(nums)):
            right=summ-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1