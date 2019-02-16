import re

def get_values(data_str):
    if isinstance(data_str, float):
        pass
    else:
        data = data_str.split(":")
        if isinstance(data, list) and len(data)>0:
            return data
        else:
            return None
def get_title(data_str):
    if isinstance(data_str, float):
        pass
    else:
        data = data_str.split("(")
        if isinstance(data, list) and len(data)>0:
            return data[0].strip()
        else:
            return None
def get_month(data_str):
    try:
        return int(data_str)
    except:
        dic={'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
                     'July':7, 'August':8, 'September':9, 'October':10, 'November':11,
                     'December':12}
        if data_str in dic:
            return dic[data_str]
        else:
            return None
def get_runtime(data_str):
    if isinstance(data_str, float):
        pass
    else:
        data=re.split(' |m|M',data_str)
        if isinstance(data, list) and len(data)>0:
            try:
                return float(data[0].strip())
            except:
                return None
        else:
            return None
def get_money(data_str):
    if isinstance(data_str, float):
        pass
    else:
        index=re.search('\d',data_str)
        if index:
            try:
                money=float(data_str[index.start():].strip())
                if (money>0):
                    return money
                else:
                    return None
            except:
                return None
        else:
            return None
def get_money_new_movies(data_str):
    if isinstance(data_str, float):
        pass
    else:
        return float(re.sub("[^0-9]", "",data_str))