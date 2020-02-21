# Fill the Python code in this file

import unittest

from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    """test module to test search function in `recursive_json_search.py` """

    def test_search_found(self):
        """key should be found, return list should not be empty"""
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        """key should not be found, should return an empty list"""
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        """Should return a list"""
        self.assertIsInstance(json_search(key1,data),list)

# Replaces function in test_json_search.py
def json_search(key,input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : keyword to be searched, case sensitive
    input_object : JSON object to be parsed
    inner_funtion() is actually doing the job
    return a list of key:value pair
    """
    ret_val=[]
    def inner_funtion(key,input_object):
        if isinstance(input_object, dict): # Handle dict
            for k, v in input_object.items():
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict):
                    inner_funtion(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)):
                            inner_funtion(key,item)
        else: # handle a list, some APIs return JSON object in a list
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_funtion(key,val)

    inner_funtion(key,input_object)
    return ret_val

if __name__ == '__main__':
        unittest.main()
