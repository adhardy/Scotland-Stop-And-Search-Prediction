from plotly.subplots import make_subplots
import plotly.graph_objects as go
import math
import statsmodels.api as sm
from matplotlib import pyplot as plt
import pandas as pd

def plot_distributions(df, cols = 4, height=2000, width=1000, cols_to_exclude=None):

    rows = math.ceil(len(df.columns) / cols) 

    subplot_titles = tuple(parameter for parameter in df.columns)
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)

    for i, col_name in enumerate(df.columns):
        row = (i // cols) + 1
        col = (i % cols) + 1
        
        fig.add_trace(go.Histogram(x=df[col_name]), row=row, col=col)
        #fig.update_xaxes(title_text=col_name, row = row, col = row)
        #fig.update_yaxes(title_text="Count", row = row, col = row)
    fig.update_layout(height=height, width=width, title="Distribution", showlegend=False)
    return fig

def plot_boxes(df, cols = 4, height=2000, width=1000, cols_to_exclude=None):

    rows = math.ceil(len(df.columns) / cols) 

    subplot_titles = tuple(parameter for parameter in df.columns)
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)

    for i, col_name in enumerate(df.columns):
        row = (i // cols) + 1
        col = (i % cols) + 1
        
        fig.add_trace(go.Box(y=df[col_name]), row=row, col=col)
        # fig.update_xaxes(title_text=col_name, row = row, col = row)
        # fig.update_yaxes(title_text="Count", row = row, col = row)
    fig.update_layout(height=height, width=width, title="Distribution", showlegend=False)
    return fig


def plotQQ(df, cols=2, height=None, width=None):

    rows = math.ceil(len(df.columns) / cols)

    if height == None:
        height = 7.5 * rows
    if width == None:
        width = 7.5 * cols

    fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(width,height))
    axs = axs.flatten()
    col_names = df.columns.to_list()

    for i, col_name in enumerate(col_names):
        sm.qqplot(data=df[col_name], fit=True, line='45', ax=axs[i])
        axs[i].set_title(f"QQ Plot of {col_name}")

    fig.show()

if __name__ == "__main__":

    df = pd.read_csv("data/simd_2020_ward.csv")
    plotQQ(df[["CIF", "EMERG", "crime_count", "crime_count_log"]])