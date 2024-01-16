from utils import write_to_json
from owl_parser import parse_owl_file, convert_graph_to_dict

def convert_owl_to_json(input_file_path, output_file_path):
    """
    Function to convert an OWL file to a JSON file
    """
    # Parse the OWL file and convert it to a RDF graph
    graph = parse_owl_file(input_file_path)
    
    # Convert the RDF graph to a dictionary
    data_dict = convert_graph_to_dict(graph)
    
    # Write the dictionary to a JSON file
    write_to_json(data_dict, output_file_path)

