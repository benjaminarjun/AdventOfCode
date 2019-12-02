import os
import sys

def _get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def get_data_file(file_name):
    return os.path.join(_get_script_path(), '..', '..', '..', 'data', file_name)
