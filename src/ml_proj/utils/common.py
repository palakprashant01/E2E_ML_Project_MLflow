# utils: functionalities we will be using frequently in our code for reusability in our code
import os
from box.exceptions import BoxValueError #we will use this instead of custom exception
import yaml
from ml_proj import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any

#we want to read yaml files
@ensure_annotations
def read_yaml(path_of_yaml: Path) -> ConfigBox: #returning as a ConfigBox:

    """
    Reading yaml files and returning as a ConfigBox
    path_of_yaml: path like input

    Raising ValueError if yaml file is empty, where e is an empty file

    Returning the content of the yaml file as a ConfigBox
    """
    try:
        with open(path_of_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_of_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
#we want to create directories for different aspects of this E2E ML Project (data ingestion, data validation, etc.)
@ensure_annotations
def create_directories(path_of_directories: list, verbose = True):
    """
    This function creates a list of directories.
    path_of_directories (list): list of directory like input paths

    This function will also ignore if multiple directories have to be created.
    """
    for path in path_of_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"Created directory here: {path}")

#We want to save json data in a file
@ensure_annotations
def save_json(path: Path, data: dict):
    #path: this is the path to the json file
    #data: this is the data to be saved within the json file
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)
    logger.info(f"json file saved here: {path}")

#We want to now load the json file and return the content as a ConfigBox
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    #path: this is the path containing the json data
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)

#We want to save binary data in a file
@ensure_annotations
def save_binary_data(data: Any, path = Path):
    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved here: {path}")

#We want to load the binary file
@ensure_annotations
def load_binary_file(path: Path) -> Any:
    #load the binary data, where path is the path to the binary file
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from {path}")
    return data

#now we want to get the size of the file
@ensure_annotations
def size(path:Path) -> str:
    #get size in KB
    #here the input is the path to the file
    size_KB = round(os.path.getsize(path)/1024)
    return f"~ {size_KB} KB"
