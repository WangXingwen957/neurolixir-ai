import time

class _TimeCalculator:
    def __init__(self):
        """Provides time duration calculations and wait functionality."""
        class _Year:
            def __init__(self, count):
                """Initialize time durations based on years."""
                self.year = count
                self.month = (self.year * 12)
                self.day = (self.month * 30)
                self.week = (self.day * 7)
                self.hour = (self.day * 24)
                self.minute = (self.hour * 60)
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified years."""
                time.sleep(self.second)
        class _Month:
            def __init__(self, count):
                """Initialize time durations based on months."""
                self.month = count
                self.year = (self.month / 12)
                self.day = (self.month * 30)
                self.week = (self.day * 7)
                self.hour = (self.day * 24)
                self.minute = (self.hour * 60)
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified months."""
                time.sleep(self.second)
        class _Day:
            def __init__(self, count):
                """Initialize time durations based on days."""
                self.day = count
                self.month = (self.day / 30)
                self.year = (self.month / 12)
                self.week = (self.day * 7)
                self.hour = (self.day * 24)
                self.minute = (self.hour * 60)
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified days."""
                time.sleep(self.second)
        class _Week:
            def __init__(self, count):
                """Initialize time durations based on weeks."""
                self.week = count
                self.year = (self.week / 52)
                self.day = (self.week * 7)
                self.hour = (self.week * 7 * 24)
                self.minute = (self.hour * 60)
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified weeks."""
                time.sleep(self.second)
        class _Hour:
            def __init__(self, count):
                """Initialize time durations based on hours."""
                self.hour = count
                self.year = (self.hour / 8760)
                self.month = (self.hour / 730)
                self.day = (self.hour / 24)
                self.week = (self.day / 7)
                self.minute = (self.hour * 60)
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified hours."""
                time.sleep(self.second)
        class _Minute:
            def __init__(self, count):
                """Initialize time durations based on minutes."""
                self.year = (count / 525600)
                self.month = (count / 43800)
                self.day = (count / 1440)
                self.week = (self.day / 7)
                self.hour = (count / 60)
                self.minute = count
                self.second = (self.minute * 60)
            
            def wait(self):
                """Pause execution for the equivalent number of seconds in the specified minutes."""
                time.sleep(self.second)
        class _Second:
            def __init__(self, count):
                """Initialize time durations based on seconds."""
                self.second = count
                self.minute = (self.second / 60)
                self.hour = (self.minute / 60)
                self.day = (self.hour / 24)
                self.week = (self.day / 7)
                self.month = (self.day / 30)
                self.year = (self.month / 12)
            
            def wait(self):
                """Pause execution for the specified number of seconds."""
                time.sleep(self.second)
        self.Year = _Year
        self.Month = _Month
        self.Day = _Day
        self.Week = _Week
        self.Hour = _Hour
        self.Minute = _Minute
        self.Second = _Second