#!/usr/bin/python3
"""
Module for XML serialization and deserialization.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Parameters:
        dictionary (dict): The Python dictionary to be serialized.
        filename (str): The name of the XML file to save the serialized data.

    Returns:
        None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and reconstruct it into a Python dictionary.

    Parameters:
        filename (str): The name of the XML file containing the serialized data.

    Returns:
        dict: A Python dictionary reconstructed from the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
