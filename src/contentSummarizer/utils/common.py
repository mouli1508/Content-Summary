import os
from box.exceptions import BoxValueError
import yaml
from contentSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return

    Args:
        path_to_yaml (str): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'YAML file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """Create directories
        
        Args:
        path_to_directory (str): Path to the directories
        ignore_log (bool, optional): ignore if multiple directories to be created. Defaults to False.
    """

    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory: {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get the size of a file in KB

    Args:
        path (Path): Path to the file
        
    Returns:
        str: size of the file in KB
    """
    size = round(os.path.getsize(path) / 1024)
    return f'~ {size} KB'