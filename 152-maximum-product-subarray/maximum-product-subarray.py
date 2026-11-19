class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_min = cur_max = result = nums[0]
        for n in nums[1:]:
            candidate = (n,cur_min*n,cur_max*n)
            cur_max = max(candidate)
            cur_min = min(candidate)
            result = max(result,cur_max)
        return result