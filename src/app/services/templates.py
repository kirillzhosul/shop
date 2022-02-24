#!env/bin/python
"""
    Merchandise shop templates service.
    Provides interfaces for some templates work.
"""

from typing import List

from os import listdir
from os.path import splitext
from os.path import join as path_join

from flask import current_app


def templates_get_name_list(*args) -> List[str]:
    """
    Returns list of template names in given path.
    :param args: List of template folder.
    :return: List of names.
    """
    templates_folder = path_join(current_app.root_path, current_app.template_folder)
    templates_path = path_join(templates_folder, *args)
    return [
        splitext(template_file)[0] for template_file in listdir(templates_path)
    ]
