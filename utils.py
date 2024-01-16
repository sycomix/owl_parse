import os
import json
import xml.etree.ElementTree as ET

def read_file(file_path):
    """
    Function to read a file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def write_to_json(data, output_path):
    """
    Function to write data to a JSON file
    """
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file)

def write_to_xml(data, output_path):
    """
    Function to write data to an XML file
    """
    tree = ET.ElementTree(data)
    tree.write(output_path)

def validate_file_extension(file_path, extension):
    """
    Function to validate the file extension
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension == extension