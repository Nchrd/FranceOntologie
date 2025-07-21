from tkinter import Tk, Label, Frame, Entry, Button, YES
from tkinter import ttk
from rdflib import RDFS, Graph, Namespace, URIRef, Literal, RDF

from rdfFilters import getClassesFromModel, getPropertiesFromModel, getLabelOrShortName, getAllDataElements
from tkinterCustom import AutocompleteCombobox
import unicodedata

def loadOntology(ontologyFile :str, classesNames :list, propertiesNames :list):
    """
    Load the ontology from the specified file.

    :param ontologyFile: The path to the ontology file.
    :type ontologyFile: str
    :param classesNames: The list to store class names.
    :type classesNames: list
    :param propertiesNames: The list to store property names.
    :type propertiesNames: list
    :return: None
    :rtype: None
    """

    # Import Ontology model from ttl file
    model = Graph()
    model.parse(ontologyFile, format="turtle")

    # Get classes and properties from the model
    classes = getClassesFromModel(model)
    for c in classes:
        classesNames.append(getLabelOrShortName(c, model))

    properties = getPropertiesFromModel(model)
    for p in properties:
        propertiesNames.append(getLabelOrShortName(p, model))
    propertiesNames.insert(0, "Aucune")

def loadData(dataFile :str):
    """
    Load the data from the specified file.

    :param dataFile: The path to the data file.
    :type dataFile: str
    :return: None
    :rtype: None
    """
    data = Graph()
    data.parse(dataFile, format="turtle")
    return data

def makeDataIndexation():
    """
    Index the data elements from the loaded data.
    :param elements: The list to store data elements.
    :type elements: list
    :return: None
    :rtype: None
    """
    # Load data from the file
    data = loadData("./../Data.ttl")
    dataURI = getAllDataElements(data)
    dataNames = list()

    for uri in dataURI:
        label = getLabelOrShortName(uri, data)
        dataNames.append(label)
    return dataURI, dataNames



classesNames = list()
propertiesNames = list()
loadOntology("./../FrOnt.ttl", classesNames, propertiesNames)

dataElementsURI, dataElementsName = makeDataIndexation()

# Create the main window
window = Tk()
window.title("France Ontologie")
window.geometry("800x600")
window.configure(bg="lightgray")
window.resizable(False, False)

# Create a label
titleLabel = Label(window, text="Insérer une donnée", font=("Arial", 24), bg="lightgray")
titleLabel.pack()

# Create a frame for the form
formFrame = Frame(window, bg="lightgray", )

# Create label for class choice
classLabel = Label(formFrame, text="Classe de la donnée :", font=("Arial", 14), bg="lightgray")
classLabel.pack()

# Create ComboBox for class selection
classComboBox = ttk.Combobox(formFrame, values=classesNames, font=("Arial", 12), width=41)
classComboBox.current(0)
classComboBox.pack()

# Create label for title choice
titleLabel = Label(formFrame, text="Nom de la donnée :", font=("Arial", 14), bg="lightgray")
titleLabel.pack()

# Create Entry for title input
titleEntry = Entry(formFrame, font=("Arial", 12), width=41)
titleEntry.pack()

# Create label for description choice
descriptionLabel = Label(formFrame, text="Description de la donnée :", font=("Arial", 14), bg="lightgray")
descriptionLabel.pack()

# Create Entry for description input
descriptionEntry = Entry(formFrame, font=("Arial", 12), width=41)
descriptionEntry.pack()

# Create label for dependency choice
dependencyLabel = Label(formFrame, text="Propriété de dépendance :", font=("Arial", 14), bg="lightgray")
dependencyLabel.pack()

# Create ComboBox for dependency selection
dependencyComboBox = ttk.Combobox(formFrame, values=propertiesNames, font=("Arial", 12), width=41)
dependencyComboBox.current(0)
dependencyComboBox.pack()

# Create label for value choice
valueLabel = Label(formFrame, text="Valeur de la dépendance :", font=("Arial", 14), bg="lightgray")
valueLabel.pack()

valueComboBox = AutocompleteCombobox(formFrame, values=dataElementsName, width=41)
valueComboBox.pack()

# Create button to submit the form
def submitForm():
    """
    Submit the form and print the values.
    :return: None
    :rtype: None
    """

    selectedClass = classComboBox.get()
    title = titleEntry.get()
    description = descriptionEntry.get()
    dependanceProperty = dependencyComboBox.get()
    dependanceValue = valueComboBox.get()

    # If the title is empty, show an error message for a few seconds
    if not title:
        errorLabel = Label(formFrame, text="Erreur : Le nom de la donnée ne peut pas être vide.", font=("Arial", 12), bg="lightgray", fg="red")
        errorLabel.pack()
        window.after(3000, errorLabel.destroy)  # Remove after 3 seconds
        return

    # If the description is empty, show an error message for a few seconds
    if not description:
        errorLabel = Label(formFrame, text="Erreur : La description de la donnée ne peut pas être vide.", font=("Arial", 12), bg="lightgray", fg="red")
        errorLabel.pack()
        window.after(3000, errorLabel.destroy)  # Remove after 3 seconds
        return
    
    FRONT = Namespace("https://nchrd.github.io/FranceOntologie/index.html#")
    # Load the existing data graph
    data_graph = Graph()
    data_graph.parse("./../Data.ttl", format="turtle")

    # Reload ontology to get property URIs
    ontology_graph = Graph()
    ontology_graph.parse("./../FrOnt.ttl", format="turtle")

    # Define normalization function
    def normalize_label(label):
        # Remove accents and convert to lowercase with underscores
        label = unicodedata.normalize('NFD', label)
        label = ''.join([c for c in label if unicodedata.category(c) != 'Mn'])
        label = label.casefold().replace(" ", "_")
        label = label.replace("'", "_")
        label = label.replace(",", "")
        return label

    # Create a new URI for the data element
    normalized_title = normalize_label(title)
    new_data_uri = FRONT[normalized_title]

    classes = getClassesFromModel(ontology_graph)
    class_uri = None
    for c in classes:
        if getLabelOrShortName(c, ontology_graph) == selectedClass:
            class_uri = c
            break

    if class_uri is None:
        errorLabel = Label(formFrame, text="Erreur : Classe sélectionnée invalide.", font=("Arial", 12), bg="lightgray", fg="red")
        errorLabel.pack()
        window.after(3000, errorLabel.destroy)
        return

    # Add triples for the new data element
    data_graph.add((new_data_uri, RDF.type, class_uri))
    data_graph.add((new_data_uri, RDFS["label"], Literal(title)))
    data_graph.add((new_data_uri, RDFS["comment"], Literal(description)))

    # Add dependency property if selected and not "Aucune"
    if dependanceProperty != "Aucune" and dependanceValue:
        # Find the URI of the dependency property from the ontology model
        try:
            properties = getPropertiesFromModel(ontology_graph)
            # Normalize title for URI creation
            normalized_title = normalize_label(title)
            new_data_uri = FRONT[normalized_title]
            property_uri = None
            for p in properties:
                if getLabelOrShortName(p, ontology_graph) == dependanceProperty:
                    property_uri = p
                    break

            value_index = dataElementsName.index(dependanceValue)
            value_uri = dataElementsURI[value_index]
            if property_uri:
                data_graph.add((value_uri, property_uri, new_data_uri))
        except ValueError:
            pass  # Value not found, skip

    # Save the updated graph back to the file
    data_graph.serialize("./../Data.ttl", format="turtle")
    
    return 0

submitButton = Button(formFrame, text="Enregistrer", command=submitForm, font=("Arial", 14), bg="lightgray")
submitButton.pack()

# Packing the form frame
formFrame.pack(expand=YES)
# Display window
window.mainloop()