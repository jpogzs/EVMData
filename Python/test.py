import scipy.io as sio
import pathlib
path = pathlib.Path(__file__).parent.resolve()
print(path)


import os

for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            print(os.path.join('', file))
            evm = os.path.join(root, file)
            my_struct = sio.loadmat(evm)
            my_struct.keys()
            data = my_struct["ThisStructure"]
            comments = my_struct["Comments"]
            notes = comments[0,0]["TechQCNotes"][0,0]            
            stringnotes = str(notes)
            techqcnotes = stringnotes.replace("['","")
            techqcnotes = techqcnotes.replace("']","")
            print(techqcnotes)

"""
import os
for x in os.listdir(path):
    if x.endswith(".evm"):
        # Prints only evm file present in My Folder
        print(x)
        
        my_struct = sio.loadmat(x)
        my_struct.keys()
        data = my_struct["ThisStructure"]
        comments = my_struct["Comments"]
        notes = comments[0,0]["TechQCNotes"][:,0]
        print(notes)
"""
"""
import scipy.io as sio
my_struct = sio.loadmat(x)
my_struct.keys()
data = my_struct["ThisStructure"]
comments = my_struct["Comments"]
notes = comments[0,0]["TechQCNotes"][:,0]
print(notes)
"""

