import argparse
from owl_parser import parse_owl_file
from xml_converter import convert_owl_to_xml
from json_converter import convert_owl_to_json

def main():
    parser = argparse.ArgumentParser(description='Convert OWL files to XML or JSON.')
    parser.add_argument('input_file', type=str, help='Path to the input OWL file.')
    parser.add_argument('output_file', type=str, help='Path to the output XML or JSON file.')
    parser.add_argument('--format', type=str, choices=['xml', 'json'], default='json', help='Output format. Default is JSON.')
    
    args = parser.parse_args()
    
    # Parse the OWL file and convert it to a RDF graph
    graph = parse_owl_file(args.input_file)
    
    # Convert the RDF graph to the desired format and write it to the output file
    if args.format == 'xml':
        convert_owl_to_xml(graph, args.output_file)
    else:  # Default is JSON
        convert_owl_to_json(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
