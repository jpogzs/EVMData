# TechQCNotes
# Extract TechQCNotes from EVM files

# Credits:
# Idea: Lawrence Trinidad
# Code: James Pogio

import scipy.io as sio
import pandas as pd
import os
import time

print("***************************************")
print("TechQCNotes")
print("Extract Tech or QC Notes from EVM files")
print("***************************************")
print("Idea: LT \t Code: Pogi")
print()
time.sleep(3)

path = os.getcwd()
# print(path)
fname = []
fnotes = []

for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            evm = ""
            my_struct = {}
            notes = ""
            evm = (os.path.join('', file))
            print(evm)
            evmpath = os.path.join(root, file)
            try:
                my_struct = sio.loadmat(evmpath)
                my_struct.keys()
                data = my_struct["ThisStructure"]
                comments = my_struct["Comments"]
                notes = comments[0,0]["TechQCNotes"][0,0] 
            except:
                print("Invalid EVM")
            
            finally:
                           
                stringnotes = str(notes)
                techqcnotes = stringnotes.replace("['","")
                techqcnotes = techqcnotes.replace("']","")
                techqcnotes = techqcnotes.replace("[","")
                techqcnotes = techqcnotes.replace("]","")
                techqcnotes = techqcnotes.replace("-","")
                print(techqcnotes)
            
                fname.append(evm)
                fnotes.append(techqcnotes)

     
# dictionary of lists
dict = {'Filename': fname, 'TechQCNotes': fnotes}
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('TechQCNotes.csv', index=False)

print()
print("********************************")
print("Done")
print("Results saved in TechQCNotes.csv")
print("********************************")
time.sleep(3)