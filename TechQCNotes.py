import scipy.io as sio
import pandas as pd
import os
import time

print("***************************************")
print("TechQCNotes v1.2")
print("Extract Tech or QC Notes from EVM files")
print("***************************************")
print("Idea: LT \t Code: Pogi")
print()
time.sleep(3)

path = os.getcwd()
# print(path)
fname = []
fnotes = []
techqcnotes = ""

for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".evm"):
            samecheck = ""
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
                #n = 0
                #t = 0
                for x in notes:
                    history = str(x)
                    #n += 1       
                     
                    #techqcnotes = techqcnotes.replace("['","")
                    #techqcnotes = techqcnotes.replace("']","")
                
                    if any (x in history for x in exclude):
                        history = ""
                    elif (samecheck == history):
                        history = ""
                        #print("same")
                    
                    else:
                        if samecheck == "":
                            techqcnotes += str(history)
                            #t = n
                            #print("same t "+str(t))
                            
                        else:         
                            if str(x) in techqcnotes:    
                                print("...")
                                #print("n " +str(n))
                                #print("t " +str(t))    
                            else:                                                                 
                                techqcnotes += "\n" + str(history)
                                #t = n
                                #print(x)
                        samecheck = history
                                     
                    #history += str(techqcnotes) + "\n"  
                    #stringnotes = str(notes)
                techqcnotes = techqcnotes.replace("[","")
                techqcnotes = techqcnotes.replace("]","")
                print(techqcnotes)
                fname.append(evm)
                fnotes.append(techqcnotes)
                history = ""
                techqcnotes = ""

     
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