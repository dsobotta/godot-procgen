# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import uuid
import os
import pathlib
import shutil
import bpy

def bl_result(task_result: bool) -> set:
    if not task_result:
        return {"CANCELED"}
    return {"FINISHED"}

def get_build_dir() -> str:
    build_dir = bpy.context.preferences.addons[__package__].preferences.build_dir
    return os.path.abspath(build_dir)

def get_tmp_dir() -> str:
    build_dir = get_build_dir()
    if not build_dir:
        return None

    return build_dir + "\\tmp"

def create_tmp_blend() -> str:
    return __create_tmp_file("blend")

def clean_build_dir() -> bool:
    return __clean_recursive( get_build_dir() )

def clean_tmp_dir() -> bool:
    return __clean_recursive( get_tmp_dir() )

### INTERNAL ###
def __create_tmp_file(extension: str) -> str:
    build_dir_path = get_build_dir()
    if not os.path.exists(build_dir_path):
        os.mkdir(build_dir_path)

    tmp_dir_path = get_tmp_dir()
    if not os.path.exists(tmp_dir_path):
        os.mkdir(tmp_dir_path)

    filename = uuid.uuid4().hex
    out_path = tmp_dir_path + "\\" + filename + "." + extension
    pathlib.Path(out_path).touch()
    return out_path

def __clean_recursive(path: str) -> bool:
    if os.path.exists(path):
        shutil.rmtree(path)

    #todo: improve error handling here
    return True

### END INTERNAL ###
