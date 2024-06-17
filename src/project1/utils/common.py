import os
from box.exceptions import BoxValueError
import yaml
from project1 import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotation
def read_yaml(yaml_path: Path) -> ConfigBox:
    """
    Read the yaml file and return the ConfigBox object

    Args:
        yaml_path (Path): Path to the yaml file
    Raises:
        ValueError: if the yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f'yaml file: {yaml_path} Successfully loaded')
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotation
def create_dir(dir_path: list, verbose= True):
    """
    Create the directory if it does not exist

    Args:
        dir_path (list): List of directory path
        ignore_log (bool, optional): Ignore the log. Defaults to True.
    """
    for path in dir_path:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok= True)
            if verbose:
                logger.info(f'Creating directory: {path}')


@ensure_annotation
def save_json(data: dict, json_path: Path):
    """
    Save the json file

    Args:
        data (dict): Data to be saved
        json_path (Path): Path to the json file
    """
    with open(json_path, 'w') as f:
        json.dump(data, f)
        
    logger.info(f'json file: {json_path} Successfully saved')

@ensure_annotation
def load_json(json_path: Path) -> ConfigBox:
    """
    Load the json file and return the ConfigBox object

    Args:
        json_path (Path): Path to the json file

    Returns:
        ConfigBox: ConfigBox type
    """
    with open(json_path, 'r') as f:
        config = json.load(f)

    logger.info(f'json file: {json_path} Successfully loaded')
    return ConfigBox(config)

@ensure_annotation
def save_bin(data: Any, bin_path: Path):
    """
    Save the binary file

    Args:
        data (Any): Data to be saved
        bin_path (Path): Path to the binary file
    """
    with open(bin_path, 'wb') as f:
        joblib.dump(data, f)

    logger.info(f'binary file: {bin_path} Successfully saved')


@ensure_annotation
def load_bin(bin_path: Path) -> Any:
    """
    Load the binary file

    Args:
        bin_path (Path): Path to the binary file

    Returns:
        Any: Loaded data
    """
    with open(bin_path, 'rb') as f:
        data = joblib.load(f)

    logger.info(f'binary file: {bin_path} Successfully loaded')
    return data

@ensure_annotation
def get_size(path: Path) -> str:
    """
    Get the size of the file

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file
    """
    size = os.path.getsize(path)
    return f'{size/1024:.2f} KB'


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImage(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string