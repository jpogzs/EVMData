# TechQCNotes
# Extract TechQCNotes from EVM files

# Code: James Pogio

import scipy.io as sio
import pandas as pd
import os
import time

print("***************************************")
print("TechQCNotes v1.5")
print("Extract Tech or QC Notes from EVM files")
print("***************************************")
print("Credits: DDQ SME Team")
print("***************************************")
time.sleep(3)

path = os.getcwd()

fname = []
notes1 = []
notes2 = []
notes3 = []
notes4 = []
notes5 = []
notes6 = []
notes7 = []
notes8 = []
notes9 = []
notes10 = []
dict = {'Filename': fname, 'Note 1': notes1}
techqcnotes = ""


def dictadd(x):
    if x == 1:
        dict.update({"Note 1": notes1})
    elif x == 2:
        dict.update({"Note 2": notes2})
    elif x == 3:
        dict.update({"Note 3": notes3})
    elif x == 4:
        dict.update({"Note 4": notes4})
    elif x == 5:
        dict.update({"Note 5": notes5})
    elif x == 6:
        dict.update({"Note 6": notes6})
    elif x == 7:
        dict.update({"Note 7": notes7})
    elif x == 8:
        dict.update({"Note 8": notes8})
    elif x == 9:
        dict.update({"Note 9": notes9})
    elif x == 10:
        dict.update({"Note 10": notes10})


for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            samecheck = ""
            notecount = 0
            note1 = ""
            note2 = ""
            note3 = ""
            note4 = ""
            note5 = ""
            note6 = ""
            note7 = ""
            note8 = ""
            note9 = ""
            note10 = ""
            evm = (os.path.join('', file))
            print(evm)
            evmpath = os.path.join(root, file)

            try:
                my_struct = sio.loadmat(evmpath)
                my_struct.keys()
                data = my_struct["ThisStructure"]
                comments = my_struct["Comments"]
                notes = comments[0, 0]["Notes"][55:, 0]

            except:
                print("\n" + "Invalid EVM")
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

                # streaming file line
                checkP = ""
                openedBy = ""
                pNote = ""
                qcNotes = ""
                popenedBy = ""
                pqcNotes = ""
                pcheckP = ""
                y = 0

                txtNotes = ""
                for x in notes:
                    y += 1
                    line = str(x)

                    # opened by
                    if "Opened by" in line:
                        split = line.split()
                        openedBy = split[2]
                    if (openedBy != popenedBy):
                        qcNotes = ""
                        if (popenedBy != "" and pqcNotes != "" and pcheckP != "" and pNote != pqcNotes):
                            txtNotes = pqcNotes.replace("['", "")
                            txtNotes = txtNotes.replace("']", "\n")
                            txtNotes = txtNotes.replace("[", "")
                            txtNotes = txtNotes.replace("]", "")

                            txtCP = pcheckP.replace("['", "")
                            txtCP = txtCP.replace("']", "")
                            txtCP = txtCP.replace("[", "")
                            txtCP = txtCP.replace("]", "")
                            txtCP = txtCP.split("by")
                            txtCP = txtCP[0]
                            txtCP = txtCP.split("as")
                            txtCP = txtCP[0]

                            print(str(notecount + 1) +
                                  " -------------------------")
                            print(popenedBy + "\n" + "\n" + txtNotes +
                                  "\n" + txtCP + "\n---------------------------")
                            txtNotes = popenedBy + "\n" + "\n" + txtNotes + "\n" + txtCP
                            pNote = pqcNotes
                            notecount += 1

                            dictadd(notecount)
                            if notecount == 1:
                                note1 += txtNotes + "\n"
                            elif notecount == 2:
                                note2 += txtNotes + "\n"
                            elif notecount == 3:
                                note3 += txtNotes + "\n"
                            elif notecount == 4:
                                note4 += txtNotes + "\n"
                            elif notecount == 5:
                                note5 += txtNotes + "\n"
                            elif notecount == 6:
                                note6 += txtNotes + "\n"
                            elif notecount == 7:
                                note7 += txtNotes + "\n"
                            elif notecount == 8:
                                note8 += txtNotes + "\n"
                            elif notecount == 9:
                                note9 += txtNotes + "\n"
                            elif notecount == 10:
                                note10 += txtNotes + "\n"

                    # exclude list
                    if not any(x in line for x in exclude):
                        #     qcNotes = ""
                        # else:
                        if (line not in pqcNotes):
                            qcNotes += line
                        else:
                            qcNotes = line

                    # checkpoint
                    if "Checkpoint" in line:
                        checkP = line

                    popenedBy = openedBy
                    pqcNotes = qcNotes
                    pcheckP = checkP

                    if (y == len(notes)):
                        pqcNotes = pqcNotes.replace(pNote, "")
                        if (popenedBy != "" and pqcNotes != "" and pcheckP != ""):

                            txtNotes = pqcNotes.replace("['", "")
                            txtNotes = txtNotes.replace("']", "\n")
                            txtNotes = txtNotes.replace("[", "")
                            txtNotes = txtNotes.replace("]", "")

                            txtCP = pcheckP.replace("['", "")
                            txtCP = txtCP.replace("']", "")
                            txtCP = txtCP.replace("[", "")
                            txtCP = txtCP.replace("]", "")
                            txtCP = txtCP.split("by")
                            txtCP = txtCP[0]
                            txtCP = txtCP.split("as")
                            txtCP = txtCP[0]

                            notecount += 1
                            print(str(notecount + 1) +
                                  " -------------------------")
                            print(openedBy + "\n" + "\n" + txtNotes +
                                  "\n" + txtCP + "\n---------------------------")
                            txtNotes = openedBy + "\n" + "\n" + txtNotes + "\n" + txtCP

                            dictadd(notecount)
                            if notecount == 1:
                                note1 += txtNotes + "\n"
                            elif notecount == 2:
                                note2 += txtNotes + "\n"
                            elif notecount == 3:
                                note3 += txtNotes + "\n"
                            elif notecount == 4:
                                note4 += txtNotes + "\n"
                            elif notecount == 5:
                                note5 += txtNotes + "\n"
                            elif notecount == 6:
                                note6 += txtNotes + "\n"
                            elif notecount == 7:
                                note7 += txtNotes + "\n"
                            elif notecount == 8:
                                note8 += txtNotes + "\n"
                            elif notecount == 9:
                                note9 += txtNotes + "\n"
                            elif notecount == 10:
                                note10 += txtNotes + "\n"


                fname.append(evm)
                notes1.append(note1)
                notes2.append(note2)
                notes3.append(note3)
                notes4.append(note4)
                notes5.append(note5)
                notes6.append(note6)
                notes7.append(note7)
                notes8.append(note8)
                notes9.append(note9)
                notes10.append(note10)

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('TechQCNotes.csv', index=False)

print()
print("********************************")
print("Done!")
print("Results saved in TechQCNotes.csv")
print("********************************")
time.sleep(3)
