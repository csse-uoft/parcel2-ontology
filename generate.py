import ontospy
import rdflib
from ontospy.gendocs.viz.viz_html_multi import *


def generate_docs(file, output_path, format=None, theme="cosmo", preview=False):
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
    model = ontospy.Ontospy(verbose=True)
    model.load_rdf(file, rdf_format=format)  # Load the ontology file
    model.build_all()
    print(model.stats())

    # Generate the HTML documentation
    v = KompleteViz(model, theme=theme)  # Instantiate the visualization object
    v.build(output_path)
    if preview: v.preview()  # Open in browser


if __name__ == "__main__":
    generate_docs("./ontologies/icontact.ttl", "./docs/icontact")
    generate_docs("./ontologies/time.ttl", "./docs/time")
    generate_docs("./ontologies/cmmp.ttl", "./docs/cmmp", format="turtle")
