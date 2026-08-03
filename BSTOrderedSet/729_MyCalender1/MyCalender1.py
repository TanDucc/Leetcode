class MyCalender:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if not (end <= s or start >= e):
                return False
        self.bookings.append((start, end))
        return True