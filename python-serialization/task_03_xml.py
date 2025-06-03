#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to XML format and saves it to a file

    Args:
        dictionary: Dictionary to serialize
        filename: Path to the output XML file
    """
    root = ET.Element("data")
    for key in dictionary:
        element = ET.SubElement(root, key)
        element.text = str(dictionary[key])
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes data from an XML file into a dictionary

    Args:
        filename: Path to the XML file

    Returns:
        Dictionary containing the deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}

    for element in root:
        result_dict[element.tag] = element.text

    return result_dict
