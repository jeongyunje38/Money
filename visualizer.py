import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from stock_analyzer import StockAnalyzer


class Visualizer:

    def __init__(self) -> None:
        pass

    @staticmethod
    def show(data:pd.DataFrame, split_dates:pd.Series) -> None:
        data.set_index("date", inplace=True)
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=("Stock Price", "Volume"),
            row_heights=[0.7, 0.3]
            )
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["open"],
                high=data["high"],
                low=data["low"],
                close=data["close"],
                name="Stock Price"
                ),
            row=1,
            col=1
            )
        fig.add_trace(
            go.Bar(
                x=data.index,
                y=data["volume"],
                name="Volume"
                ),
            row=2,
            col=1
            )
        for date in split_dates.index:
            fig.add_annotation(
                x=date,
                y=data.loc[date, "close"],
                text="Split",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="red",
                font=dict(size=10, color="red"),
                align="center",
                row=1,
                col=1
            )
        fig.update_layout(width=600, height=800, showlegend=False)
        fig.update_xaxes(rangeslider_visible=False)
        st.plotly_chart(fig)
