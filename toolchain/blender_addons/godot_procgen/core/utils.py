# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

# Line too long
# pylint: disable=C0301

import uuid
import os
import pathlib
import shutil
import bpy

def get_toplevel_package() -> str:
    return "godot_procgen"

def bl_result(task_result: bool) -> set:
    if not task_result:
        return {"CANCELLED"}
    return {"FINISHED"}

def create_dir(path: str) -> bool:
    if not os.path.exists(path):
        os.makedirs(path)

    #todo: better error handling
    return True

def bl_get_curr_file() -> str:
    return bpy.data.filepath

def bl_open_file(file: str) -> bool:
    if not os.path.exists(file):
        print("GDPG: failed to open file: " + file)
        return False

    bpy.ops.wm.open_mainfile(filepath=file)
    return True

def bl_save_as_file(file: str) -> bool:
    if not create_dir(os.path.dirname(file)):
        return False

    bpy.ops.wm.save_as_mainfile(filepath=file)
    return True

def get_project_dir() -> str:
    project_file_path = bpy.context.preferences.addons[get_toplevel_package()].preferences.project_file

    if not project_file_path:
        print("GDPG ERROR: get_project_dir() failed to find valid project file")
        return None

    dirname = os.path.dirname(project_file_path)
    return os.path.abspath(dirname)

def get_source_dir() -> str:
    return os.path.join(get_project_dir(), "blender_src")

def get_build_dir() -> str:
    return os.path.join(get_project_dir(), "build")

def get_tmp_dir() -> str:
    return os.path.join(get_build_dir(), "tmp")

def get_variants_dir() -> str:
    return os.path.join(get_build_dir(), "variants")

def get_binary_dir() -> str:
    return os.path.join(get_build_dir(), "binary")

def get_godot_generated_dir() -> str:
    return os.path.join(get_project_dir(), "godot", "generated")

def create_tmp_blend() -> str:
    return __create_tmp_file("blend")

def clean_build_dir() -> bool:
    return __clean_recursive( get_build_dir() )

def clean_tmp_dir() -> bool:
    return __clean_recursive( get_tmp_dir() )

### INTERNAL ###
def __create_tmp_file(extension: str) -> str:
    create_dir(get_build_dir())

    tmp_dir_path = get_tmp_dir()
    create_dir(tmp_dir_path)

    filename = uuid.uuid4().hex
    out_path = os.path.join(tmp_dir_path, filename + "." + extension)
    pathlib.Path(out_path).touch()
    return out_path

def __clean_recursive(path: str) -> bool:
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("GDPG: Cleaned path: " + path)
    else:
        print("GDPG: Path already clean: " + path)

    #todo: improve error handling here
    return True

### END INTERNAL ###
