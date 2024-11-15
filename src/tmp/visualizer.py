import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots


class Visualizer:

    def __init__(self) -> None:
        pass

    @staticmethod
    def show(
        data: pd.DataFrame,
        split_dates: pd.Series = None,
        pred: pd.DataFrame = None,
        sma: pd.Series = None,
    ) -> None:
        data.set_index("date", inplace=True)
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=("Stock Price", "Volume"),
            row_heights=[0.7, 0.3],
        )
        if pred is not None:
            fig.add_trace(
                go.Scatter(
                    x=pred.index.tolist() + pred.index.tolist()[::-1],
                    y=pred["upper_ci"].tolist() + pred["lower_ci"].tolist()[::-1],
                    fill="toself",
                    fillcolor="light yellow",
                    line=dict(color="yellow"),
                    hoverinfo="skip",
                    name="CI",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=pred.index,
                    y=pred["forecast"],
                    mode="lines",
                    line=dict(color="Brown", width=2),
                    name="Forecast",
                ),
                row=1,
                col=1,
            )
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["open"],
                high=data["high"],
                low=data["low"],
                close=data["close"],
                name="Price",
            ),
            row=1,
            col=1,
        )
        if sma is not None:
            colors = ["red", "blue", "green", "purple", "orange", "cyan"]
            for i, (window, sma_values) in enumerate(sma.items()):
                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=sma_values,
                        mode="lines",
                        line=dict(color=colors[i % len(colors)], width=1),
                        name=f"SMA {window}",
                    ),
                    row=1,
                    col=1,
                )
        fig.add_trace(
            go.Bar(x=data.index, y=data["volume"], name="Volume", marker_color="pink"),
            row=2,
            col=1,
        )
        if split_dates is not None:
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
                    col=1,
                )
        fig.update_layout(width=600, height=800, showlegend=True)
        fig.update_xaxes(rangeslider_visible=False)
        st.plotly_chart(fig)
