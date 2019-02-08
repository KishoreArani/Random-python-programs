'''
A simple porgram to check internet Connection of laptop/pc.
'''


from requests import get
from requests import exceptions
def internetConnection():
    try:
        get('http://google.com',timeout = 3)
        print("connected")
    except exceptions.ConnectionError:
        print("not connected")


internetConnection()

