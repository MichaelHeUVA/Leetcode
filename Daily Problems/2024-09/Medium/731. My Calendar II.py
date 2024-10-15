# https://leetcode.com/problems/my-calendar-ii/description/?envType=daily-question&envId=2024-09-27


class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if not (end <= s or start >= e):
                return False
        for s, e in self.calendar:
            if not (end <= s or start >= e):
                self.overlaps.append((max(start, s), min(end, e)))
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
