import requests
import urllib.parse
import json

from config import GATEWAY_IP
from config import GATEWAY_PORT
from config import API_PROJECT_NAME




def unit_tests(suite='all'):
    """asset, all, ..."""

    x = requests.get('http://{gateway_ip}:{gateway_port}/system/webdev/{api_project_name}/unit-tests'.format(gateway_ip=GATEWAY_IP, gateway_port=GATEWAY_PORT, api_project_name=API_PROJECT_NAME),
                     params={'suite':suite})



def tag_read(tagPath):

    encodedPath = urllib.parse.quote(tagPath)
    x = requests.get('http://{gateway_ip}:{gateway_port}/system/webdev/{api_project_name}/tag-read'.format(gateway_ip=GATEWAY_IP, gateway_port=GATEWAY_PORT, api_project_name=API_PROJECT_NAME), 
                     params={'tagPath':encodedPath})
    
    if x.status_code == 200:
        return x.json()
    else:
        return {}


def rpc(functionPath, args=[], kwargs={}):
    functionPathEncoded = urllib.parse.quote(functionPath)
    argsEncoded = urllib.parse.quote(json.dumps(args))
    kwargsEncoded = urllib.parse.quote(json.dumps(kwargs))
    x = requests.get('http://{gateway_ip}:{gateway_port}/system/webdev/{api_project_name}/rpc'.format(gateway_ip=GATEWAY_IP, gateway_port=GATEWAY_PORT, api_project_name=API_PROJECT_NAME),
                     params={'functionPath':functionPathEncoded, 'args': argsEncoded, 'kwargs': kwargsEncoded})
    
    if x.status_code == 200:
        return True
    else:
        return False