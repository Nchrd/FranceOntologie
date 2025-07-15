from rdflib import Graph, RDFS, RDF, URIRef
import re

def getLabelOrShortName(uri: str, g: Graph) -> str:
    """
    Get the label or short name of a URI from the RDF graph.

    :param uri: The URI to get the label or short name for.
    :type uri: str
    :param g: The RDF graph to search in.
    :type g: Graph
    :return: The label or short name of the URI.
    :rtype: str
    """
    
    for label in g.objects(URIRef(uri), RDFS.label):
        return str(label)
    
    uri = str(uri)
    if '#' in uri:
        uri = uri.split("#")[-1]
    elif '/' in uri:
        uri = uri.split("/")[-1]

    uri = re.sub(r"p[0-9]+_", "", uri, count=1)
    return uri

def getClassesFromModel(g: Graph) -> list:
    """
    Get all the classes from the RDF Model.
    
    :param g: The RDF model to search in.
    :type g: Graph
    
    :return: A list of classes in the model.
    :rtype: list
    """
    classes = list()
    for s, p, o in g.triples((None, RDF.type, None)):
        if o == RDFS.Class:
            classes.append(s)
    return classes

def getPropertiesFromModel(g: Graph) -> list:
    """
    Get all the properties from the RDF Model.
    
    :param g: The RDF model to search in.
    :type g: Graph
    
    :return: A list of properties in the model.
    :rtype: list
    """
    properties = list()
    for s, p, o in g.triples((None, RDF.type, None)):
        if o == RDF.Property:
            properties.append(s)
    return properties

def getAllDataElements(g: Graph) -> list:
    """
    Get all the data elements from the RDF Model.
    
    :param g: The RDF model to search in.
    :type g: Graph
    
    :return: A list of data elements in the model.
    :rtype: list
    """
    dataElements = list()
    for s, p, o in g.triples((None, RDF.type, None)):
        dataElements.append(s)
    return dataElements