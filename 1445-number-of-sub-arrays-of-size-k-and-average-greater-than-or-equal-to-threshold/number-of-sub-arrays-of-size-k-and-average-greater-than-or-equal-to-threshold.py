class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window=sum(arr[:k])
        maxT=k*threshold
        count=0
        if window>=maxT:
            count+=1
        for i in range(k,len(arr)):
            window=window+arr[i]
            window=window-arr[i-k]
            if window>=maxT:
                count+=1
        return count