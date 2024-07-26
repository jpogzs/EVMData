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
print("TechQCNotes v1.4")
print("Extract Tech or QC Notes from EVM files")
print("***************************************")
print("Idea: LT \t Code: Pogi")
print()
# time.sleep(3)

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

# def noteadd(nc, n):
#     if nc == 1:
#         global note1
#         note1 = n
#     elif nc == 2:
#         global note2
#         note2 = n

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
                tNote = ""
                cP = ""
                prev = ""
                curr = ""
                pNote = ""
                cNote = ""
                empT = 0
                qcTech = ""
                checkPoint = ""
                qcNotes = ""
                for x in notes:
                    line = str(x)
                    # cp = ""


                    line = line.replace("['","")
                    line = line.replace("']","")
                    line = line.replace("[","")
                    line = line.replace("]","")


                    #opened by
                    if "Opened by" in line:
                        split = line.split()
                        noteby = split[2]

                        #if in exclude list

                    cNote = line
                    if any (x in line for x in exclude):
                        cNote += ""
                    else:
                        if (cNote in pNote):
                            # print("sameNote")                            
                            empT = 0
                            qcNotes = ""
                        else:
                            # cNote += line
                            print(cNote)
                            qcNotes = cNote
                            # tnValid = True
                            empT = 1
                            
                    checkPoint = ""
                    if "Checkpoint" in line:
                        cP = line
                        curr = noteby
                        if (curr != prev and empT == 1):                            
                            # print(curr + " " + cP)
                            qcTech = curr
                            checkPoint = cP
                        # elif (empT == True):
                        #     print("")
                        else:
                            # print("sameQC")
                            qcTech = ""
                                           
                   

                    pNote += cNote
                    prev = curr

                    qcNotes = pNote
                    checkPoint = cP
                    qcTech = prev

                    if (qcTech != "" and checkPoint != "" and qcNotes != ""):
                        print(qcTech + "\n" + checkPoint + "\n" + qcNotes + "\n")





                




                    



                    






                    # #if in exclude list
                    # if not (x in line for x in exclude):
                    #     line = ""

                    # elif line == "":
                    #     line = ""                        

                    # #if same notes as previous
                    # elif (samecheck == line):
                    #     line = ""
                    
                    # else:
                    #     #1st note
                    #     if samecheck == "":
                    #         notecount = 1   
                    #         dictadd(notecount)
                    #         techqcnotes += noteby + ":\n" + line + "\n"
                    #         # print(techqcnotes)
                    #         # noteadd(notecount, techqcnotes)
                    #         note1 += noteby + ":\n" + line + "\n"
                    #         # note1 += line + "\n"
                            
                    #     #additional notes    
                    #     else:  
                    #         #if same note    
                    #         if line in note1 or line in note2 or line in note3 or line in note4 or line in note5 or line in note6 or line in note7 or line in note8 or line in note9 or line in note10:    
                    #             print("...")
                            
                    #         #not same note
                    #         else:      
                    #             if samenoteby == noteby:
                    #                 techqcnotes += line + cP + "\n"
                    #                 # print(techqcnotes)
                    #                 # # noteadd(notecount, techqcnotes) 
                    #                 if notecount == 1:
                    #                     note1 += line + "\n"
                    #                 elif notecount == 2:
                    #                     note2 += line + "\n"
                    #                 elif notecount == 3:
                    #                     note3 += line + "\n"
                    #                 elif notecount == 4:
                    #                     note4 += line + "\n"
                    #                 elif notecount == 5:
                    #                     note5 += line + "\n"
                    #                 elif notecount == 6:
                    #                     note6 += line + "\n"
                    #                 elif notecount == 7:
                    #                     note7 += line + "\n"
                    #                 elif notecount == 8:
                    #                     note8 += line + "\n"
                    #                 elif notecount == 9:
                    #                     note9 += line + "\n"
                    #                 elif notecount == 10:
                    #                     note10 += line + "\n"
                    #             else:     
                    #                 notecount += 1                                    
                    #                 dictadd(notecount)    
                    #                 techqcnotes += noteby + ":\n" + line + "\n"
                    #                 # print(techqcnotes)
                    #                 # noteadd(notecount, techqcnotes)                                       
                                    
                    #                 if notecount == 1:
                    #                     note1 += noteby + ":\n" + line + "\n"
                    #                     # note1 += line + "\n"
                    #                 elif notecount == 2:
                    #                     note2 += noteby + ":\n" + line + "\n"
                    #                     # note2 += line + "\n"
                    #                 elif notecount == 3:
                    #                     note3 += noteby + ":\n" + line + "\n"
                    #                     # note3 += line + "\n"
                    #                 elif notecount == 4:
                    #                     note4 += noteby + ":\n" + line + "\n"
                    #                     # note4 += line + "\n"
                    #                 elif notecount == 5:
                    #                     note5 += noteby + ":\n" + line + "\n"
                    #                     # note5 += line + "\n"
                    #                 elif notecount == 6:
                    #                     note6 += noteby + ":\n" + line + "\n"
                    #                     # note6 += line + "\n"
                    #                 elif notecount == 7:
                    #                     note7 += noteby + ":\n" + line + "\n"
                    #                     # note7 += line + "\n"
                    #                 elif notecount == 8:
                    #                     note8 += noteby + ":\n" + line + "\n"
                    #                     # note8 += line + "\n"
                    #                 elif notecount == 9:
                    #                     note9 += noteby + ":\n" + line + "\n"
                    #                     # note9 += line + "\n"
                    #                 elif notecount == 10:
                    #                     note10 += noteby + ":\n" + line + "\n"
                    #                     # note10 += line + "\n"

                    #     samecheck = line
                    #     samenoteby = noteby
                                     
                # print(techqcnotes)
                # fname.append(evm)                
                # notes1.append(note1)
                # notes2.append(note2)
                # notes3.append(note3)
                # notes4.append(note4)
                # notes5.append(note5)
                # notes6.append(note6)
                # notes7.append(note7)
                # notes8.append(note8)
                # notes9.append(note9)
                # notes10.append(note10)
                # line = ""
                # techqcnotes = ""
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('TechQCNotes.csv', index=False)

print()
print("********************************")
print("Done")
print("Results saved in TechQCNotes.csv")
print("********************************")
time.sleep(3)