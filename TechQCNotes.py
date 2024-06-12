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
print("TechQCNotes v1.3")
print("Extract Tech or QC Notes from EVM files")
print("***************************************")
print("Idea: LT \t Code: Pogi")
print()
time.sleep(3)

path = os.getcwd()
# print(path)
fname = []
notes1 = []
notes2 = []
techqcnotes = ""

for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            samecheck = ""
            notecount = 0
            note1 = ""
            note2 = ""
            evm = (os.path.join('', file))
            print(evm)
            evmpath = os.path.join(root, file)

            try:
                my_struct = sio.loadmat(evmpath)
                my_struct.keys()
                data = my_struct["ThisStructure"]
                comments = my_struct["Comments"]
                notes = comments[0,0]["Notes"][55:,0]    
            
            except:
                print("Invalid EVM")
                notes = []
                

            finally:        
                exclude = ["Opened by",
                           "from TW as Checkpoint by",
                           "Saved by",
                           "Checkpoint upon Finish",
                           "Measurement Completed from TW by",
                           "Checkpoint upon Reject",
                           "Rejected in QC from TW as",
                           "Rejected from TW as",
                           "from TW by",
                           "Shipped by awshrcacher",
                           "History_New"]

                #streaming file line
                for x in notes:
                    line = str(x)

                    line = line.replace("['","")
                    line = line.replace("']","")
                    line = line.replace("[","")
                    line = line.replace("]","")

                    #opened by
                    if "Opened by" in line:
                        split = line.split()
                        noteby = split[2]

                    #if in exclude list
                    if any (x in line for x in exclude):
                        line = ""

                    elif line == "":
                        line = ""                        

                    #if same notes as previous
                    elif (samecheck == line):
                        line = ""
                    
                    else:
                        #1st note
                        if samecheck == "":
                            notecount = 1   
                            # techqcnotes += noteby + ":\n" + line + "\n"
                            note1 += noteby + ":\n" + line + "\n"
                            
                        #additional notes    
                        else:  
                            #if same note    
                            if line in note1 or line in note2:    
                                print("...")

                            # elif noteby in techqcnotes:
                            #     print("shit")
                            
                            #not same note
                            else:      
                                if samenoteby == noteby:
                                    # techqcnotes += line + "\n"
                                    if notecount == 1:
                                        note1 += line + "\n"
                                    elif notecount == 2:
                                        note2 += line + "\n"
                                else:     
                                    notecount += 1                                             
                                    # techqcnotes += noteby + ":\n" + line + "\n"
                                    if notecount == 1:
                                        note1 += noteby + ":\n" + line + "\n"
                                    elif notecount == 2:
                                        note2 += noteby + ":\n" + line + "\n"

                        samecheck = line
                        samenoteby = noteby
                                     

                # note1 = note1.replace("['","")
                # note1 = note1.replace("']","")
                # note1 = note1.replace("[","")
                # note1 = note1.replace("]","")
                print(techqcnotes)
                fname.append(evm)
                notes1.append(note1)
                notes2.append(note2)
                line = ""
                techqcnotes = ""

     
# dictionary of lists
dict = {'Filename': fname, 'Note 1': notes1, 'Note 2': notes2}
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('TechQCNotes.csv', index=False)

print()
print("********************************")
print("Done")
print("Results saved in TechQCNotes.csv")
print("********************************")
time.sleep(3)