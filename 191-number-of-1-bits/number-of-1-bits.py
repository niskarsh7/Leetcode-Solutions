class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_no=format(n,"b")
        arr=[int(x) for x in binary_no]
        count=0
        for i in range(len(arr)):
            if arr[i]==1:
                count+=1
        return count
        