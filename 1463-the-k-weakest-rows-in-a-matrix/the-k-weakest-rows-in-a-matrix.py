class Solution:
    def binarySearch(self,arr):
        low=0
        high=len(arr)-1
        while low<high:
            mid = low + (high-low)//2
            if arr[mid]==1:
                low=mid+1
            else:
                high=mid
        return len(arr) if arr[low]==1 else low           
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        row_details=[]
        for i in range(n):
            count=self.binarySearch(mat[i])
            row_details.append((count,i))
        row_details.sort(key=lambda x:(x[0],x[1]))
        return [row_details[i][1] for i in range(k)]    