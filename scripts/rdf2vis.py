from rdflib import Graph, RDFS, RDF
from rdflib.tools.rdfs2dot import rdfs2dot
from pyvis.network import Network
from os import system

from rdfFilters import getLabelOrShortName

# Create a Graph
g = Graph()
# Parse in an RDF file hosted on the Internet
g.parse("./../Data.ttl")

def generateModelImage(g: Graph):
    """
    Generates a PNG image from an RDFS graph using the rdfs2dot tool.
    
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
    :note: The function only works with RDFS graphs, aka Ontology classes and properties declarations.
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

def generateDataHtmlGraph(g: Graph, outputFile: str = "data.html"):
    """
    Generates a PNG image from an RDF graph using pyvis tool.
    
    :param g: An RDF graph to be converted to a PNG image.
    :type g: Graph
    :param outputFile: The output file name for the generated HTML file.
    :type outputFile: str
    :raises Exception: If the graph is empty or if there are issues with the graph.
    :return: None
    :rtype: None
    :example:
    >>> g = Graph()
    >>> g.parse("./../data.ttl")
    >>> generateDataImage(g)
    >>> # Generates a Html File from the RDF graph.
    """

    # Create a pyvis Network
    net = Network(directed=True)
    #net.barnes_hut()
    net.force_atlas_2based()
    net.set_options('{ "physics": { "forceAtlas2Based": { "gravitationalConstant": -20, "centralGravity": 0.001, "springLength": 300, "springConstant": 0.2 }, "maxVelocity": 50, "solver": "forceAtlas2Based", "timestep": 0.35, "stabilization": { "iterations": 100 } } }')



    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")
        
        # Ignore comments
        if pred == RDFS.comment:
            continue

        # Ignore RDFS types
        if pred == RDF.type:
            continue

        # Ignore RDFS Labels
        if pred == RDFS.label:
            continue
        
        # Get the label or short name for the subject, predicate, and object
        subj_label = getLabelOrShortName(subj, g)
        obj_label = getLabelOrShortName(obj, g)
        pred_label = getLabelOrShortName(pred, g)

        # Add nodes and edges to the pyvis Network
        net.add_node(str(subj), label=subj_label, shape="ellipse")
        net.add_node(str(obj), label=obj_label, shape="ellipse")
        net.add_edge(str(subj), str(obj), label=pred_label)

    # Generate the HTML file
    net.write_html("../" + outputFile)

generateDataHtmlGraph(g, "test.html")