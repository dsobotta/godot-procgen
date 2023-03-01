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

# Too few public methods OMEGALUL
# pylint: disable=R0903

import os
import pathlib
import random
import bpy
from .. import core

class GenVariants(core.buildstep.BuildStep):

    __base_name = ""
    __rel_path = ""
    __tmp_filepath = ""
    __num_variants = 1

    def __init__(self, operand: str, **kwargs):
        self.__base_name = pathlib.Path(operand).stem
        rel_filename = os.path.relpath(operand, core.utils.get_source_dir())
        self.__rel_path = os.path.dirname(rel_filename)
        self.__num_variants = kwargs.get('variants', 5)
        self.__tmp_filepath = core.utils.create_tmp_blend()
        core.utils.bl_open_file(operand)
        core.utils.bl_save_as_file(self.__tmp_filepath)

    def print_inputs(self, geo_node: bpy.types.NodesModifier):
        modifier_name = geo_node.name
        print("GDPG modifier: " + modifier_name)
        for node_input in geo_node.node_group.inputs:
            identifier = node_input.identifier
            is_int = isinstance(node_input, bpy.types.NodeSocketInterfaceInt)
            is_float = isinstance(node_input, bpy.types.NodeSocketInterfaceFloat)
            if is_int or is_float:
                input_name = node_input.name
                value = bpy.context.object.modifiers[modifier_name].get(identifier)
                print(input_name + " -- " + str(value))

    def randomize_inputs(self, geo_node: bpy.types.NodesModifier):
        modifier_name = geo_node.name
        print("GDPG randomizing inputs of modifier: " + modifier_name)
        for node_input in geo_node.node_group.inputs:
            identifier = node_input.identifier
            #input_name = node_input.name
            if isinstance(node_input, bpy.types.NodeSocketInterfaceInt):
                min_value = node_input.min_value
                max_value = node_input.max_value
                if min_value != max_value:
                    value = random.randrange(min_value, max_value)
                    #print(input_name + " -- " + str(value))
                    bpy.context.object.modifiers[modifier_name][identifier] = value
                continue
            if isinstance(node_input, bpy.types.NodeSocketInterfaceFloat):
                min_value = node_input.min_value
                max_value = node_input.max_value
                if min_value != max_value:
                    value = random.uniform(min_value, max_value)
                    #print(input_name + " -- " + str(value))
                    bpy.context.object.modifiers[modifier_name][identifier] = value
                continue

    def run(self) -> bool:
        out_dir = os.path.join(core.utils.get_variants_dir(), self.__rel_path, self.__base_name)
        core.utils.create_dir(out_dir)

        for i in range(self.__num_variants):
            #re-open temp file (before mesh conversion) so we don't have to spam undo operations
            core.utils.bl_open_file(self.__tmp_filepath)

            variant_name = self.__base_name + str(i+1)

            #https://blenderartists.org/t/bad-context-after-open-new-file-with-python/1398392
            for w in bpy.context.window_manager.windows:
                s = w.screen
                for a in s.areas:
                    if a.type == "VIEW_3D":
                        with bpy.context.temp_override(window=w, area=a):
                            bpy.ops.object.mode_set(mode='OBJECT')
                            bpy.ops.object.select_all(action='DESELECT')

                            #todo: handle multiple exporting multiple invariant objects from one source file
                            for obj in bpy.data.objects:
                                obj.select_set(True)
                                for modifier in bpy.context.object.modifiers:
                                    if isinstance(modifier, bpy.types.NodesModifier):
                                        self.randomize_inputs(modifier)
                                        self.print_inputs(modifier)

                                bpy.ops.object.convert(target='MESH')
                                obj.name = variant_name + "_genobj"
                                obj.data.name = "genmesh"
                                obj.select_set(False)
                            break

            path = os.path.join(out_dir, variant_name + ".blend")
            core.utils.bl_save_as_file(path)

        self._cleanup()

        return True

    def _cleanup(self) -> None:
        pass
