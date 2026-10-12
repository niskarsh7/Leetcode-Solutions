class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        res=[]
        i=0
        while i < len(arr):
            if arr[i]==0:
                res.append(0)
                res.append(0)
            else:
                res.append(arr[i])
            i+=1
        arr[:]=res[:len(arr)]

            
        """
        Do not return anything, modify arr in-place instead.
        """
        