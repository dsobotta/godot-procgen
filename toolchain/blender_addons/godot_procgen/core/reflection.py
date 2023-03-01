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

import random
import bpy

def print_inputs(geo_node: bpy.types.NodesModifier):
    modifier_name = geo_node.name
    print("GDPG modifier: " + modifier_name)
    for node_input in geo_node.node_group.inputs:
        identifier = node_input.identifier
        is_int = isinstance(node_input, bpy.types.NodeSocketInterfaceInt)
        is_float = isinstance(node_input, bpy.types.NodeSocketInterfaceFloat)
        if is_int or is_float:
            value = bpy.context.object.modifiers[modifier_name].get(identifier)
            debug_data = [
                node_input.name,
                str(value)
            ]
            print(debug_data)

def nsi_by_name(modifier: bpy.types.NodesModifier, input_name: str) -> bpy.types.NodeSocketInterface:
    for node_input in modifier.node_group.inputs:
        if input_name == node_input.name:
            return node_input
    return None

# def get_input_by_name(modifier: bpy.types.NodesModifier, input_name: str, value):
#     nsi = nsi_by_name(modifier, input_name)
#     if nsi is None:
#         print("Error, failed to find NodeSocketInterface with name: " + input_name)
#         return 0

#     return bpy.context.object.modifiers[modifier.name].get(nsi.identifier)

#returns the value that was set
def set_input_by_name(modifier: bpy.types.NodesModifier, input_name: str, value):
    nsi = nsi_by_name(modifier, input_name)
    if nsi is None:
        print("Error, failed to find NodeSocketInterface with name: " + input_name)
        return 0

    bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
    return value

#returns the value that was set
def randomize_input_byname(modifier: bpy.types.NodesModifier, input_name: str):
    nsi = nsi_by_name(modifier, input_name)
    if nsi is None:
        print("Error, failed to find NodeSocketInterface with name: " + input_name)
        return 0
    return randomize_input(modifier, nsi)

#returns the value that was set
def randomize_input(modifier: bpy.types.NodesModifier, nsi: bpy.types.NodeSocketInterface):
    if isinstance(nsi, bpy.types.NodeSocketInterfaceInt):
        min_value = nsi.min_value
        max_value = nsi.max_value
        if min_value == max_value:
            return min_value

        value = random.randrange(min_value, max_value)
        bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
        return value

    if isinstance(nsi, bpy.types.NodeSocketInterfaceFloat):
        value = random.uniform(nsi.min_value, nsi.max_value)
        bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
        return value

    return 0

def randomize_all_inputs(modifier: bpy.types.NodesModifier) -> None:
    print("GDPG randomizing inputs of modifier: " + modifier.name)
    for nsi in modifier.node_group.inputs:
        randomize_input(modifier, nsi)
