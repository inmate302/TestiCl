import os
import pygame

def parse_gamecontrollerdb(file_path):
    """
    Parses the contents of the SDL gamecontrollerdb.txt file and returns a dictionary
    mapping controller GUIDs to their corresponding button/axis mappings.
    """
    controller_mappings = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split(',')
                guid = parts[0]
                #name = parts[1]
                mapping = ','.join(parts[2:])
                controller_mappings[guid] = mapping

    return controller_mappings

def get_default_mapping(controller_guid, controller_mappings):
    """
    Looks up the default button/axis mapping for the given controller GUID in the
    controller_mappings dictionary. Returns the mapping as a dictionary.
    """
    if controller_guid in controller_mappings:
        mapping = controller_mappings[controller_guid]
        mapping_parts = mapping.split(',')
        default_mapping = {}

        for i, value in enumerate(mapping_parts):
            if value.startswith('b'):
                # try:
                default_mapping[i] = value
                default_mapping[i] = ''.join(c for c in default_mapping[i] if c.isdigit())
               
                #except ValueError:
                    # Ignore invalid values
                    #pass
            elif value.startswith('a'):
                axis_value = value.split(':')
                if len(axis_value) == 2:
                    #try:
                    default_mapping[i] = axis_value[1][1:]
                    #except ValueError:
                        # Ignore invalid values
                       # pass
                else:
                    try:
                        default_mapping[i] = axis_value[0][1:]
                    except ValueError:
                        # Ignore invalid values
                        pass
            else:
                try:
                    default_mapping[i] = value
                    default_mapping[i] = ''.join(c for c in default_mapping[i] if c.isdigit())
                except ValueError:
                    # Ignore invalid values
                    pass

        return default_mapping
    #else:
        #return None
