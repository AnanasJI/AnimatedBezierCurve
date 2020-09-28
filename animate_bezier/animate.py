import numpy as np
from seaborn import color_palette
from altair_saver import save
from os.path import expanduser

from ._internal.helper_functions import create_df_dict, num_decimals
from ._internal.visualisation import create_visualisation, draw_curve_segment


def animate_bezier(
    xs: np.ndarray,
    ys: np.ndarray,
    step: float,
    filename: str = "bezier",
    download_folder: str = expanduser("~") + "/Downloads/",
) -> None:
    ts = np.arange(0, 1 + step, step)
    ts = np.round_(ts, decimals=num_decimals(step))
    colours = color_palette("rocket", len(xs))
    colours = list(
        map(
            lambda tuple: "#%02x%02x%02x"
            % (int(tuple[0] * 255), int(tuple[1] * 255), int(tuple[2] * 255)),
            colours,
        )
    )

    dfs = create_df_dict(np.vstack((xs, ys)).T, ts)
    chart = create_visualisation(dfs, ts, colours)

    for i in range(len(dfs[1]) - 1):
        row = dfs[1].iloc[i]
        row2 = dfs[1].iloc[i + 1]
        xs = np.hstack((row.loc["x"], row2.loc["x"]))
        ys = np.hstack((row.loc["y"], row2.loc["y"]))
        chart += draw_curve_segment(xs, ys, colours[0], 0.2)

    chart = chart.interactive()

    save(chart, f"{download_folder}/{filename}.html")


if __name__ == "__main__":
    phi = np.linspace(0, 2.0 * np.pi, 10)
    r = 0.5 + np.cos(phi)  # polar coords
    x, y = r * np.cos(phi), r * np.sin(phi)  # convert to cartesian

    x = np.linspace(0, 2 * np.pi, 10)
    y = np.cos(x)

    animate_bezier(x, y, 0.05, "filename3")
