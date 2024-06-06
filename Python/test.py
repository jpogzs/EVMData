import scipy.io as sio
import pathlib
path = pathlib.Path(__file__).parent.resolve()
print(path)

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
import scipy.io as sio
my_struct = sio.loadmat(x)
my_struct.keys()
data = my_struct["ThisStructure"]
comments = my_struct["Comments"]
notes = comments[0,0]["TechQCNotes"][:,0]
print(notes)
"""