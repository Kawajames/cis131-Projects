# File Name: Time Class - CIS131
# Description: This script defines the Time class which stores time as the total number of seconds since midnight.
# Author: Dakota Kartchner 
# Date Created: 3/1/2025

class Time:
    """Class Time with read write properties, storing time as total seconds since midnight."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize a Time object using hour, minute, and second values."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        self._total_seconds = hour * 3600 + minute * 60 + second

    @property
    def hour(self):
        """Return the hour component."""
        return self._total_seconds // 3600

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        # Preserve current minute and second values.
        minute = self.minute
        second = self.second
        self._total_seconds = hour * 3600 + minute * 60 + second

    @property
    def minute(self):
        """Return the minute component."""
        return (self._total_seconds % 3600) // 60

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        # Preserve current hour and second values.
        hour = self.hour
        second = self.second
        self._total_seconds = hour * 3600 + minute * 60 + second

    @property
    def second(self):
        """Return the second component."""
        return self._total_seconds % 60

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        # Preserve current hour and minute values.
        hour = self.hour
        minute = self.minute
        self._total_seconds = hour * 3600 + minute * 60 + second

    def set_time(self, hour=0, minute=0, second=0):
        """Set the time by updating hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def time(self):
        """Return hour, minute and second as a tuple."""
        return (self.hour, self.minute, self.second)

    @time.setter
    def time(self, time_tuple):
        """Set time from a tuple containing hour, minute, and second."""
        if len(time_tuple) != 3:
            raise ValueError("Time tuple must have exactly three elements: (hour, minute, second)")
        self.set_time(*time_tuple)

    def __repr__(self):
        """Return the official string representation of the Time object."""
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"

    def __str__(self):
        """Return a string representation of the Time object in 12-hour clock format."""
        hour_12 = 12 if self.hour in (0, 12) else self.hour % 12
        return f"{hour_12}:{self.minute:02}:{self.second:02} {'AM' if self.hour < 12 else 'PM'}"