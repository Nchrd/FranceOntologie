from tkinter import *
from tkinter import ttk

from rdflib import Graph

from rdfFilters import getClassesFromModel, getPropertiesFromModel, getLabelOrShortName

# Import Ontology model from ttl file
model = Graph()
model.parse("./../FrOnt.ttl")

# Get classes and properties from the model
classes = getClassesFromModel(model)
classesNames = list()
for c in classes:
    classesNames.append(getLabelOrShortName(c, model))

properties = getPropertiesFromModel(model)
propertiesNames = list()
for p in properties:
    propertiesNames.append(getLabelOrShortName(p, model))

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

# Packing the form frame
formFrame.pack(expand=YES)
# Display window
window.mainloop()