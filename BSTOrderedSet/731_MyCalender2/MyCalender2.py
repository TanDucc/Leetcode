class MyCalender:
    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.overlapping:
            if not (endTime <= start or startTime >= end):
                return False
        for start, end in self.non_overlapping:
            if not (endTime <= start or startTime >= end):
                self.overlapping.append((max(start, startTime), min(end, endTime)))
        self.non_overlapping.append((startTime, endTime))
        return True