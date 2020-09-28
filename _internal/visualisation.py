from typing import Dict, List

import altair as alt
import numpy as np
import pandas as pd


def create_visualisation(
    df_dic: Dict[int, pd.DataFrame], ts: np.ndarray, colours: List[str]
) -> alt.Chart:
    time_field = "t"
    select_time = alt.selection_single(
        name="select",
        fields=[time_field],
        init={time_field: min(ts)},
        bind=alt.binding_range(min=min(ts), max=max(ts), step=ts[1] - ts[0]),
    )
    chart = (
        alt.Chart(pd.DataFrame({"x": [0], "y": [0]}))
        .mark_point(opacity=0)
        .encode(x="x", y="y")
        .add_selection(select_time)
    )

    for k, df in df_dic.items():
        for t in ts:
            df_t = df[df["t"] == t]
            df_t.sort_index()
            base = alt.Chart(df_t).transform_filter(select_time)
            chart += base.mark_line(color=colours[k - 1]).encode(
                alt.X("x:Q"), alt.Y("y:Q"), alt.OpacityValue(1)
            ).transform_filter(select_time) + base.mark_point(
                color=colours[k - 1]
            ).encode(
                alt.X("x:Q"), alt.Y("y:Q"), alt.OpacityValue(1)
            ).transform_filter(
                select_time
            )
    return chart.interactive()


def draw_curve_segment(xs, ys, colour, opacity):
    df = pd.DataFrame({"x": xs, "y": ys})
    return alt.Chart(df).mark_line(opacity=opacity, color=colour).encode(x="x", y="y")
