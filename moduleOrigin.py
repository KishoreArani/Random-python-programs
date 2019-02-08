'''
Program to check the origin of the modules
'''


import math
import requests
def getOrigin(module):
    val = module.__spec__.origin
    flag = False
    if val == 'built-in':
        flag = True
    return flag

#import the respective module before checking its origin
getOrigin(math)
