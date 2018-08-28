import random
import gc
import tkinter
#print('Name generator')

# Open file and read it
streetcomposition_text_file = open("StreetComposition.txt", "r")
streetcomposition = streetcomposition_text_file.readlines()

lowclassstreetdetail_text_file = open("LowClassStreetDetail.txt", "r")
lowclassstreetdetail = lowclassstreetdetail_text_file.readlines()

highclassstreetdetail_text_file = open("HighClassStreetDetail.txt", "r")
highclassstreetdetail = highclassstreetdetail_text_file.readlines()

exteriorscent_text_file = open("ExteriorScent.txt", "r")
exteriorscent = exteriorscent_text_file.readlines()

exteriorsounds_text_file = open("ExteriorSounds.txt", "r")
exteriorsounds = exteriorsounds_text_file.readlines()

buildingtypes_text_file = open("BuildingTypes.txt", "r")
buildingtypes = buildingtypes_text_file.readlines()

residentalbuildings_text_file = open("ResidentalBuildings.txt", "r")
residentalbuildings = residentalbuildings_text_file.readlines()

businesstypes_text_file = open("BusinessTypes.txt", "r")
businesstypes = businesstypes_text_file.readlines()

# Randomize
randomstreetcomposition = random.randint(1,len(streetcomposition))
randomlowclassstreetdetail = random.randint(1,len(lowclassstreetdetail))
randomhighclassstreetdetail = random.randint(1,len(highclassstreetdetail))
randomexteriorscent = random.randint(1,len(exteriorscent))
randomexteriorsounds = random.randint(1,len(exteriorsounds))
randombuildingtypes = random.randint(1,len(buildingtypes))
randomresidentalbuildings = random.randint(1,len(residentalbuildings))
randombusinesstypes = random.randint(1,len(businesstypes))

# Write it out
# print('The name:',firstlines[randomfirstname-1].strip("\n"),lastlines[randomlastname-1].strip("\n"))

# Window handler
root = tkinter.Tk()
tkinter.Label(root,justify=left,text="Shadowrun Atmosphere Generator").grid(row=0,column=0)
tkinter.Label(root,text="Street composition:").grid(row=1,column=0)
tkinter.Label(root,text=streetcomposition[randomstreetcomposition-1].strip("\n")).grid(row=1,column=1)
tkinter.Label(root,text="Low class street detail:").grid(row=2,column=0)
tkinter.Label(root,text=lowclassstreetdetail[randomlowclassstreetdetail-1].strip("\n")).grid(row=2,column=1)
tkinter.Label(root,text="High class street detail:").grid(row=3,column=0)
tkinter.Label(root,text=highclassstreetdetail[randomhighclassstreetdetail-1].strip("\n")).grid(row=3,column=1)
tkinter.Label(root,text="Exterior scent:").grid(row=4,column=0)
tkinter.Label(root,text=exteriorscent[randomexteriorscent-1].strip("\n")).grid(row=4,column=1)
tkinter.Label(root,text="Exterior sounds:").grid(row=5,column=0)
tkinter.Label(root,text=exteriorsounds[randomexteriorsounds-1].strip("\n")).grid(row=5,column=1)
tkinter.Label(root,text="Building types:").grid(row=6,column=0)
tkinter.Label(root,text=buildingtypes[randombuildingtypes-1].strip("\n")).grid(row=6,column=1)
tkinter.Label(root,text="Residental buildings:").grid(row=7,column=0)
tkinter.Label(root,text=residentalbuildings[randomresidentalbuildings-1].strip("\n")).grid(row=7,column=1)
tkinter.Label(root,text="Business types:").grid(row=8,column=0)
tkinter.Label(root,text=businesstypes[randombusinesstypes-1].strip("\n")).grid(row=8,column=1)
root.mainloop()


#Mappaválasztás
#Mappában lévő fájlok megszámolása
#For ciklusban felolvasni a fájlokat és egyedi tömbökbe helyezni őket
#Mindegyiknek saját generált értéket adni
#Visszaadni az értékeket (fájlnév, generált érték)
#Formázás