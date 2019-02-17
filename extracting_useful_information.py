import numpy as np
import ast

#Utility functions to extract data from the original movies metadata database
def get_day(x):
  day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  try:
    answer = x.weekday()
    return day_order[answer]
  except:
    return np.nan

def get_values(data_str):
    if isinstance(data_str, float):
        pass
    else:
        values = []
        data = ast.literal_eval(data_str)
        if isinstance(data, list) and len(data)>0:
            for k_v in data:
                values.append(k_v['name'])
            return values
        else:
            return None

def get_director(data_str):
    if isinstance(data_str, float):
        pass
    else:
        values = []
        data = ast.literal_eval(data_str)
        if isinstance(data, list) and len(data)>0:
            for k_v in data:
                if('job' in k_v):
                    if(k_v['job']=='Director'):
                        values.append(k_v['name'])
            return values
        else:
            return None
