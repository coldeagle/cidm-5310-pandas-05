import matplotlib.pyplot as plt
import pandas as pd


def scatter(ax: plt.Axes, grouped_results, type: str):
    for name, grouped in grouped_results:
        ax.scatter(
            grouped['Date'],
            grouped['Close'],
            label=f'{name} Closing ({type})'
        )
    return ax


def plot_compare(ax: plt.Axes, data: pd.DataFrame, style: str, color: str, type: str, lw=None, marker=None, markersize=None):
    ax.plot(data['Date'],
            data['Close'],
            marker=marker,
            markersize=markersize,
            linestyle=style,
            lw=lw,
            color=color,
            label=f'{data["symbol"]} Closing ({type})',
    )

    return ax
