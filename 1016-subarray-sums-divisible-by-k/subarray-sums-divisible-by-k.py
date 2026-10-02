class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hashmap={}
        hashmap[0]=1
        prefix=0
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix%k
            if rem<0:
                rem+=k
            if rem in hashmap:
                count+=hashmap.get(rem)
            hashmap[rem]=hashmap.get(rem,0)+1
        return count