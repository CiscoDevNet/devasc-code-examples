# Fill the Python code in this file

from test_data import *
def json_search(key,input_object):
    ret_val=[]
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp={k:v}
                ret_val.append(temp)
            if isinstance(v, dict):
                json_search(key,v)
            elif isinstance(v, list):
                for item in v:
                    if not isinstance(item, (str,int)):
                        json_search(key,item)
    else:
        for val in input_object:
            if not isinstance(val, (str,int)):
                json_search(key,val)
    return ret_val
