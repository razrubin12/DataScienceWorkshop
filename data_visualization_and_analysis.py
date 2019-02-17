import pandas as pd
import matplotlib.pylab as plt
from matplotlib import cm as cm
import numpy as np
import seaborn as sns

# Given a data frame and a column creates a histogram of the column
def counting_values(df, column):
    value_count = {}
    for row in df[column].dropna():
        if len(row) > 0:
            for key in row:
                if key in value_count:
                    value_count[key] += 1
                else:
                    value_count[key] = 1
        else:
            pass
    return value_count

# Receives labels for a plot and adds them to plt
def set_graph_labels(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

# Recieves a dataframe and creates a correlation matrix for it
def correlation_matrix(df):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(False)
    plt.title('Feature Correlation Matrix')

    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    labels = list(df.columns.values)
    ax1.set_xticks(np.arange(len(labels)))
    ax1.set_yticks(np.arange(len(labels)))
    ax1.set_xticklabels(labels, fontsize=10, rotation=90)
    ax1.set_yticklabels(labels, fontsize=10)
    fig.colorbar(cax)
    plt.show()

# Creates a box plot from the dataframe and x, y values
def high_order_categorical_boxplot(df, x, y, selected=[], ylim=6e8):
    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(data=df[x].apply(lambda x: pd.Series(x))
                     .stack()
                     .reset_index(level=1, drop=True)
                     .to_frame(x)
                     .join(df.drop([x], axis=1), how='left'),
                     x=x, y=y, order=selected)
    ax.set_ylim([0, ylim])

# Creates a count plot from the dataframe and x, y values
def high_order_categorical_countplot(df, col, selected=[]):
    if len(selected) == 0:
        selected = df[col].apply(pd.Series).stack().unique()
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df[col].apply(lambda x: pd.Series(x))
                  .stack()
                  .reset_index(level=1, drop=True)
                  .to_frame(col)
                  .join(df.drop([col], axis=1), how='left'),
                  x=col, order=selected)
