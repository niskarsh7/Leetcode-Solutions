class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        result=[intervals[0]]
        i=1 
        while i < len(intervals):
            prev=result[-1]
            curr=intervals[i]
            if curr[0]>=prev[0] and curr[1]<=prev[1]:
                pass
            else:
                result.append(curr)
            i+=1
        return len(result)