import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm as cm
from matplotlib.pyplot import figure
from IPython.display import display
from sklearn.preprocessing import MultiLabelBinarizer
import ast
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn import neural_network
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import scale
import sys
import re
import warnings
warnings.simplefilter('ignore')
import data_combine_from_git
import scraped_data_integration
import extracting_useful_information
import data_visualization_and_analysis