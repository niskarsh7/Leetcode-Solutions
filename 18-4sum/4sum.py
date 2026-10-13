class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res=[]
        for left in range(len(nums)-3):
            if left>0 and nums[left]==nums[left-1]:
                continue
            for right in range(len(nums)-1,left+2,-1):
                if right<len(nums)-1 and nums[right]==nums[right+1]:
                    continue
                i=left+1
                j=right-1
                while i<j:
                    if nums[left]+nums[i]+nums[j]+nums[right]==target:
                        res.append([nums[left],nums[i],nums[j],nums[right]])
                        i+=1 
                        j-=1
                        while i<j and nums[i]==nums[i-1]:
                            i+=1
                        while i<j and nums[j]==nums[j+1]:
                            j-=1
                    elif nums[left]+nums[i]+nums[j]+nums[right]>target:
                        j-=1
                    else:
                        i+=1
        return res