import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pmdarima import auto_arima


class StockPredictor:

    def __init__(self) -> None:
        self.us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())

    def predict_using_auto_arima(self, data:pd.Series, periods:int) -> pd.DataFrame:
        model = auto_arima(
            y=data,
            d=1,
            start_p=0,
            max_p=3,
            start_q=0,
            max_q=3,
            m=1,
            seasonal=False,
            stepwise=True
            )
        forecast, ci = model.predict(n_periods=periods, return_conf_int=True)
        forecast_index = pd.date_range(
            start=pd.to_datetime(data.index)[-1] + pd.Timedelta(days=1),
            periods=periods,
            freq=self.us_bd
            )
        results = pd.DataFrame({
            "forecast": forecast.values,
            "lower_ci": ci[:, 0],
            "upper_ci": ci[:, 1]
        }, index=forecast_index)
        return results
