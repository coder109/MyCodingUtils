"""
This module provides utility functions for working with Data Structures.
"""

import re

def remove_empty_str(lst):
    """
    Removes empty strings from a list of strings.

    Args:
        lst (list): list of strings

    Returns:
        list: list of strings with empty strings removed
    """
    result = []
    for e in lst:
        if e.strip() != "":
            result.append(e)
    return result

def remove_duplicate_in_list(lst):
    """
    Removes duplicate elements from a list.

    Args:
        lst (list): list containing elements

    Returns:
        list: list with duplicate elements removed
    """
    return list(set(lst))

def remove_empty_char_in_lst(lst):
    """
    Removes empty characters from a list of strings.

    Args:
        lst (list): list of strings

    Returns:
        list: list of strings with empty characters removed
    """
    result = []
    for e in lst:
        result.append(e.strip())
    return result

def remove_chinese_and_japanese_chars(text):
    """
    Removes Chinese and Japanese characters from a string.

    Args:
        text (str): string

    Returns:
        str: string with Chinese and Japanese characters removed
    """
    pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF]')
    return pattern.findall(text)