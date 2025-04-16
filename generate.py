import ontospy
import rdflib
from ontospy.gendocs.viz.viz_html_multi import *
import os
import sys


def generate_docs(file, output_path, format=None, theme="cosmo", preview=False, title=None):
    """
    Generate documentation for the ontology using Ontospy and the HTML multi-page visualization.
    """
    # Try to parse the file with rdflib to check if it's valid RDF
    try:
        g = rdflib.Graph()
        g.parse(file, format=format)  # Specify the format if known
    except Exception as e:
        print(f"Error parsing RDF file: {e}")
        return

    # Load the ontology
    model = ontospy.Ontospy(verbose=True)  # Instantiate the Ontospy object
    model.load_rdf(file, rdf_format=format)  # Load the ontology file
    model.build_all()
    print(model.stats())

    # Generate the HTML documentation
    v = KompleteViz(model, theme=theme, title=title)  # Instantiate the visualization object
    v.build(output_path)
    if preview: v.preview()  # Open in browser

if __name__ == "__main__":
    # Read all files in the ./ontologies directory and generate documentation for each
    ontologies_dir = "./ontologies"
    output_dir = "./docs"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(ontologies_dir):
        file_path = os.path.join(ontologies_dir, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            output_path = os.path.join(output_dir, os.path.splitext(file_name)[0])
            print(f"Generating documentation for {file_path}...")
            generate_docs(file_path, output_path,)
