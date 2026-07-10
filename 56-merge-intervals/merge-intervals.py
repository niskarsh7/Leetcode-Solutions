class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            last=result[len(result)-1]
            curr=intervals[i]
            if last[1]>=curr[0]:
                last[0]=min(last[0],curr[0])
                last[1]=max(last[1],curr[1])
            else:
                result.append(curr)
        return result