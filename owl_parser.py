import os
from rdflib import Graph
from utils import read_file, validate_file_extension

def parse_owl_file(file_path):
    """
    Function to parse an OWL file and convert it to a RDF graph
    """
    if not validate_file_extension(file_path, '.owl'):
        raise ValueError(f"{file_path} is not a valid OWL file.")
    
    data = read_file(file_path)
    
    g = Graph()
    g.parse(data=data, format='xml')
    
    return g

def convert_graph_to_dict(graph):
    """
    Function to convert a RDF graph to a dictionary
    """
    data_dict = {}
    
    for subj, pred, obj in graph:
        if not (subj, pred) in data_dict:
            data_dict[(subj, pred)] = []
        data_dict[(subj, pred)].append(str(obj))
    
    return data_dict
