"""
This module provides utility functions for working with files.
Encoding:
    When a file is opened, the encoding is set to UTF-8.
Saving:
    You should call save_into_file or save_in_json or save_in_jsonl, 
    rather than rewrite_** or write_**.
"""

import json
import os

def read_file(file_path):
    """
    Reads a file and returns its content as a list of lines.

    Args:
        file_path (str): path to the file

    Returns:
        list: list of strings, each being a line in the file
    """
    fp = open(file_path, "r", encoding="UTF-8")
    return fp.readlines()

def rewrite_into_file(content, file_path):
    """
    Rewrites the content of the file at the given file path.

    Args:
        content (str or list): content to be written into the file
        file_path (str): path to the file

    Returns:
        None
    """
    fp = open(file_path, "w", encoding="UTF-8")
    if type(content) == type(["List"]):
        for content_elem in content:
            fp.write(content_elem.strip() + "\n")
    else:
        fp.write(content)

def write_into_file(content, file_path):
    """
    Appends the given content into the file at the given file path.

    Args:
        content (str or list): content to be written into the file
        file_path (str): path to the file

    Returns:
        None
    """
    fp = open(file_path, "a", encoding="UTF-8")
    if type(content) == type(["List"]):
        for content_elem in content:
            fp.write(content_elem.strip() + "\n")
    else:
        fp.write(content)

def save_into_file(content, file_path):
    """
    Saves the given content into the file at the given file path.
    
    If the file already exists, the content is rewritten into the file.
    If the file does not exist, the content is appended into the file.
    
    Args:
        content (str or list): content to be written into the file
        file_path (str): path to the file
    """
    if os.path.exists(file_path):
        rewrite_into_file(content, file_path)
    else:
        write_into_file(content, file_path)    

# List of dicts -> l_o_d
def rewrite_into_json(l_o_d, file_name):
    """
    Rewrites the given list of dictionaries into the given file as JSON object.

    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file
    """
    with open(file_name, "w") as f:
        json.dump(l_o_d, f, ensure_ascii=False)

def write_into_json(l_o_d, file_name):
    """
    Appends the given list of dictionaries into the file as a JSON object.

    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file

    Returns:
        None
    """    
    with open(file_name, "a+") as f:
        json.dump(l_o_d, f, ensure_ascii=False)

def write_into_jsonl(l_o_d, file_name):
    """
    Appends the given list of dictionaries into the file as JSON lines.

    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file

    Returns:
        None
    """
    with open(file_name, "a+") as outfile:
        for entry in l_o_d:
            json.dump(entry, outfile, ensure_ascii=False)
            outfile.write('\n')

def rewrite_into_jsonl(l_o_d, file_name):
    """
    Rewrites the given list of dictionaries into the file as JSON lines.

    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file

    Returns:
        None
    """
    
    with open(file_name, "w") as outfile:
        for entry in l_o_d:
            json.dump(entry, outfile, ensure_ascii=False)
            outfile.write('\n')

def save_in_jsonl(l_o_d, file_name):
    """
    Saves the given list of dictionaries into the given file as JSON lines.
    
    If the file already exists, the content is rewritten into the file.
    If the file does not exist, the content is appended into the file.
    
    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file
    """
    if os.path.exists(file_name):
        rewrite_into_jsonl(l_o_d, file_name)
    else:
        write_into_jsonl(l_o_d, file_name)

def save_in_json(l_o_d, file_name):
    """
    Saves the given list of dictionaries into the given file as JSON object.

    If the file already exists, the content is rewritten into the file.
    If the file does not exist, the content is appended into the file.
    
    Args:
        l_o_d (list): list of dictionaries
        file_name (str): path to the file
    """
    if os.path.exists(file_name):
        rewrite_into_json(l_o_d, file_name)
    else:
        write_into_json(l_o_d, file_name)

def remove_if_exist(file):
    """
    Removes the given file if it exists.
    
    Args:
        file (str): path to the file
    """
    if os.path.exists(file):
        os.remove(file)