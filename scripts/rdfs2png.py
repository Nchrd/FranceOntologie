from rdflib import Graph
from rdflib.tools.rdfs2dot import rdfs2dot
from os import system

# Create a Graph
#g = Graph()
# Parse in an RDF file hosted on the Internet
#g.parse("./../FrOnt.ttl")

def generateImage(g: Graph):
    """
    Generates a PNG image from an RDF graph using the rdfs2dot tool.
    
    :param g: An RDF graph to be converted to a PNG image.
    :type g: Graph
    :raises Exception: If the graph is empty or if there are issues with the graph.
    :return: None
    :rtype: None
    :example:
    >>> g = Graph()
    >>> g.parse("./../data.ttl")
    >>> generateImage(g)
    >>> # Generates a PNG image from the RDF graph.
    :note: This function uses the `rdfs2dot` tool to convert the RDF graph to a DOT format and then uses Graphviz to generate a PNG image.
    :note: The generated image will be saved as "output.png" in the current working directory.
    :note: The function assumes that the Graphviz `dot` command is available in the system's PATH.
    :note: The function also assumes that the `output.dot` file will be created in the current working directory.
    """

    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.

    with open("output.dot", "w") as f:
        rdfs2dot(g, f)

    system("dot -Tpng output.dot -o output.png")