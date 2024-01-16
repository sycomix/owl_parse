import xml.etree.ElementTree as ET
from utils import write_to_xml
from owl_parser import convert_graph_to_dict

def convert_dict_to_xml(data_dict):
    """
    Function to convert a dictionary to an XML tree
    """
    root = ET.Element('root')
    for (subj, pred), objs in data_dict.items():
        subj_element = ET.SubElement(root, 'Subject', name=str(subj))
        pred_element = ET.SubElement(subj_element, 'Predicate', name=str(pred))
        for obj in objs:
            ET.SubElement(pred_element, 'Object', name=str(obj))
    return ET.ElementTree(root)

def convert_owl_to_xml(graph, output_path):
    """
    Function to convert an OWL graph to an XML file
    """
    data_dict = convert_graph_to_dict(graph)
    xml_tree = convert_dict_to_xml(data_dict)
    write_to_xml(xml_tree, output_path)

