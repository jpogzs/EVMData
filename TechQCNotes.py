import scipy.io as sio
import pathlib
import pandas as pd
import os

path = os.getcwd()
# print(path)
fname = []
fnotes = []

for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            evm = (os.path.join('', file))
            print(evm)
            evmpath = os.path.join(root, file)
            my_struct = sio.loadmat(evmpath)
            my_struct.keys()
            data = my_struct["ThisStructure"]
            comments = my_struct["Comments"]
            notes = comments[0,0]["TechQCNotes"][0,0]            
            stringnotes = str(notes)
            techqcnotes = stringnotes.replace("['","")
            techqcnotes = techqcnotes.replace("']","")
            print(techqcnotes)
            fname.append(evm)
            fnotes.append(techqcnotes)

     
# dictionary of lists
dict = {'Filename': fname, 'TechQCNotes': fnotes}
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('TechQCNotes.csv', index=False)