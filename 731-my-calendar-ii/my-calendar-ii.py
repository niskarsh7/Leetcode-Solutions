class MyCalendarTwo:
    bookings=[]
    overlapBooking=[]
    def __init__(self):
        self.bookings=[]
        self.overlapBooking=[]
        
    def overlap(self,i1,s2,e2):
        self.s1=i1[0]
        self.e1=i1[1]

        return self.e1>=s2 and e2>=self.s1
    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.bookings)==0:
            self.bookings.append([startTime,endTime-1])
            return True

        for i in range(len(self.overlapBooking)):
            if self.overlap(self.overlapBooking[i],startTime,endTime-1):
                return False
        
        for i in range(len(self.bookings)):
            if self.overlap(self.bookings[i],startTime,endTime-1):
                self.overlapBooking.append(
                    [max(self.bookings[i][0],startTime),
                    min(self.bookings[i][1],endTime-1)]

                )
        self.bookings.append([startTime,endTime-1])
        return True    


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)