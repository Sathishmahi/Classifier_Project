import yaml
import json
from pathlib import Path
from CNN_Classifier.constant import *
import os
# from CNN_Classifier import 



def make_dirs(dir_list:list):
    try:
        for dir_name in dir_list:
            os.makedirs(dir_name,exist_ok=True)
    except Exception as e:
        raise e
def read_yaml(yaml_path:Path=CONFIG_YAML_FILE_PATH)->dict:
    try:
        
        with open(yaml_path) as yaml_file:
            content=yaml.safe_load(yaml_file)
        return content

    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e

def write_yaml()->bool:
    pass

def read_json()->dict:
    pass

def write_json()->bool:
    pass