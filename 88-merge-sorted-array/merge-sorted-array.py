class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res=[0]*(m+n)
        i=0
        j=0
        k=0
        while i < m and j <n:
            if nums1[i]<=nums2[j]:
                res[k]=nums1[i]
                k+=1
                i+=1
            else:
                res[k]=nums2[j]
                k+=1
                j+=1
        while i <m:
            res[k]=nums1[i]
            k+=1
            i+=1
        while j < n:
            res[k]=nums2[j]
            k+=1
            j+=1
        for i in range(len(res)):
            nums1[i]=res[i]