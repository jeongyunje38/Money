from pandas import DatetimeIndex, date_range
from datetime import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


class DateUtils:

    def __init__(self):
        pass

    @staticmethod
    def US_bd(fr: datetime, to: datetime):
        return date_range(
            start=fr,
            end=to,
            freq=CustomBusinessDay(calendar=USFederalHolidayCalendar()),
        )

    @staticmethod
    def right_before_bd(dates: DatetimeIndex, ref: datetime):
        return dates[dates < ref].max()

    @staticmethod
    def right_after_bd(dates: DatetimeIndex, ref: datetime):
        return dates[dates > ref].min()
