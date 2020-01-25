#Convert simples adresses at cheat readable by CTRPF
#Script by Reshiban and luc_ha for GBATemp
#Also thx at NaN (NotaName) community for his help!

#lpc = Lines Per Cheat



#------------------------------------------------
#START THE SCRIPT
#------------------------------------------------



import shutil
dest1 = shutil.copyfile("./ExportedAddresses.txt", "./cheats.txt")

#--------------------SET-LPC---------------------
lpc = 25
#--------------------SET-LPC---------------------


#Check and stock the number of file lines
print("Opening test.txt...")
nmbrlines = 0
f = open("test.txt", 'r')
print("Calculating number of lines...")
for line in f:
    nmbrlines += 1
print("Total number of lines is:", nmbrlines)
print("")


#Stock nmbrlines for futures actions
nmbrlinesStock = nmbrlines


#Calculates the last lines
while nmbrlines > lpc:
    nmbrlines = nmbrlines - lpc
linesfin = nmbrlines
print("You finish by",linesfin,"lines!")



#Set lots of values at 0
f = open("test.txt", 'a')
it = 0
serie = 0
fix = 0
fix2 = 1
nmbrPackets = 0
step = 0


#------------------------------------------------
#DELETE ALL ": " IF PRESENT
#------------------------------------------------


#Remlace all the ": " by " "
with open("test.txt","r+") as f:
    text = f.read().replace(": ","")

with open("test.txt", "w") as f:
    f.write(text)


#------------------------------------------------
#PUT SPACES TO SET A LIMIT FOR CHEATS
#------------------------------------------------


#Pass 1 line for the first line
with open("test.txt","r+") as f:
        text = f.readlines()
        text.insert(0,"\n")
        f.seek(0)
        f.writelines(text)


#Regive the number of lines
nmbrlines = 0
f = open("test.txt", 'r')
print("Calculating number of lines...")
for line in f:
    nmbrlines += 1
print("Total number of lines is:", nmbrlines)
print("")


#Def the limitations
limitation = (nmbrlines / (lpc + 2)) + 1

#Jump 2 lines every (lpc) lines
while limitation > it:
    with open("test.txt","r+") as f:
        text = f.readlines()
        text.insert(lpc+fix2+(serie*(lpc+fix)),"\n\n")
        f.seek(0)
        f.writelines(text)
        it = it + 1
        serie = serie + 1
        fix = 2
        nmbrPackets = nmbrPackets + 1


#------------------------------------------------
#ADD NAME FOR ALL CHEATS
#------------------------------------------------


it = 0
fix = 0
fix2 = 0


#Mark [* Step] for each packages
while limitation >= step - 1:
    with open("test.txt","r+") as f:
            steptext = f"[{step + 1} Step]"
            text = f.readlines()
            text.insert((lpc +2) * step,steptext)
            #print(text)
            f.seek(0)
            f.writelines(text)
            it = it + lpc + 2
            step = step + 1


#------------------------------------------------
#ADD "IF" FUNCTIONS
#------------------------------------------------


it = -1
fix = 0
fix2 = 1
serie = 0


#Add code at all the (lpc) lines
while limitation > it:
    with open("test.txt","r+") as f:
        text = f.readlines()
        text.insert(lpc+fix+fix2+(serie*lpc),"DD000000 00000200\n\nD0000000 00000000\nDD000000 00000100\n\nD0000000 00000000\n")
        #print(text)
        f.seek(0)
        f.writelines(text)
        it = it + 1
        serie = serie + 1
        fix = fix + 8
        nmbrPackets = nmbrPackets + 1


#------------------------------------------------
#COPY ADRESSES IN "IF" PARTS
#------------------------------------------------


it = -1
fix = 0
fix3 = lpc + 3
fix4 = 5
serie = 0
nmbrPackets = 0



#Copy lpc adresses in some places (1/2)
while limitation -1 > it:
    with open("test.txt","r+") as f:
        text = f.readlines()
        addr = text[:(serie * (6 + (lpc*3))) + lpc + 2]  +  text[(serie * (6 + (lpc*3))) + fix2:(serie * (6 + (lpc*3))) + lpc + fix2]   +   text[(serie * (6 + (lpc*3))) + fix3:(serie * (6 + (lpc*3))) + lpc + fix4]   +   text[(serie * (6 + (lpc*3))) + fix2:(serie * (6 + (lpc*3))) + lpc + fix2]  +  text[(serie * (6 + (lpc*3))) + lpc + 6:]
        f.seek(0)
        f.write("".join(addr))
    it = it + 1
    serie = serie + 1
    fix = fix + 8
    fix2 = 1


fix3 = linesfin + 3


#Copy lpc adresses in some places (2/2)
with open("test.txt","r+") as f:
    text = f.readlines()
    addr = text[:(serie * (6 + (lpc*3))) + linesfin + 2]  +  text[(serie * (6 + (lpc*3))) + fix2:(serie * (6 + (lpc*3))) + linesfin + fix2]   +   text[(serie * (6 + (lpc*3))) + fix3:(serie * (6 + (lpc*3))) + linesfin + fix4]   +   text[(serie * (6 + (lpc*3))) + fix2:(serie * (6 + (lpc*3))) + linesfin + fix2]  +  text[(serie * (6 + (lpc*3))) + linesfin + 6:]
    f.seek(0)
    f.write("".join(addr))
it = it + 1
serie = serie + 1
fix = fix + 8
fix2 = 1



#------------------------------------------------
#
#------------------------------------------------



it = -1
fix = 0
fix3 = lpc + 3
fix4 = 5
serie = 0
nmbrPackets = 0


#"""
#Replace all the "3F800000" by "3F000000" for L (1/2)
while limitation -1 > it:
    with open("test.txt", "r") as f:
        linesL = f.readlines()

    with open("test.txt", "w") as f:
        for i in range(((serie * ((lpc * 3) + 6)) + lpc + 2)   ,   ((serie * ((lpc * 3) + 6)) + (lpc * 2) + 2)):
            linesL[i] = linesL[i].replace("3F800000", "3F000000")
        f.write("".join(linesL))
    it = it + 1
    serie = serie + 1
    fix = fix + 8
    fix2 = 1
#"""


#"""
#Replace all the "3F800000" by "3F000000" for L (2/2)
with open("test.txt", "r") as f:
    linesL = f.readlines()

with open("test.txt", "w") as f:
    for i in range(((serie * ((lpc * 3) + 6)) + linesfin + 2)   ,   ((serie * ((lpc * 3) + 6)) + (linesfin * 2) + 4)):
        linesL[i] = linesL[i].replace("3F800000", "3F000000")
    f.write("".join(linesL))
it = it + 1
serie = serie + 1
fix = fix + 8
fix2 = 1
#"""




it = -1
fix = 0
fix3 = lpc + 3
fix4 = 5
serie = 0
nmbrPackets = 0


#"""
#Replace all the "3F800000" by "4000000" for R (1/2)
while limitation -1 > it:
    with open("test.txt", "r") as f:
        linesR = f.readlines()

    with open("test.txt", "w") as f:
        for i in range(((serie * ((lpc * 3) + 6)) + (lpc * 2) + 2)   ,   ((serie * ((lpc * 3) + 6)) + (lpc * 3) + 4)):
            linesR[i] = linesR[i].replace("3F800000", "40000000")
        f.write("".join(linesR))
    it = it + 1
    serie = serie + 1
    fix = fix + 8
    fix2 = 1
#"""


#"""
#Replace all the "3F800000" by "4000000" for R (2/2)
with open("test.txt", "r") as f:
    linesR = f.readlines()

with open("test.txt", "w") as f:
    for i in range(((serie * ((lpc * 3) + 6)) + (linesfin * 2) + 2)   ,   ((serie * ((lpc * 3) + 6)) + (linesfin * 3) + 4)):
        linesR[i] = linesR[i].replace("3F800000", "40000000")
    f.write("".join(linesR))
it = it + 1
serie = serie + 1
fix = fix + 8
fix2 = 1
#"""



#------------------------------------------------
#END OF PROGRAM
#------------------------------------------------



#Regive the number of lines
nmbrlines = 0
f = open("test.txt", 'r')
print("Calculating number of lines...")
for line in f:
    nmbrlines += 1
print("Total number of lines is:", nmbrlines)
print("")
f.close()
