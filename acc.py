#Convert simples adresses at cheat readable by CTRPF
#Script by Reshiban and luc_ha for GBATemp
#Also thx to NaN (NotaName) community for his help!

#lpc == Lines Per Cheat



#------------------------------------------------
#----------------START THE SCRIPT----------------
#------------------------------------------------

#Copy "ExportedAddresses.txt" to -> "cheats.txt"
import shutil
dest1 = shutil.copyfile("./ExportedAddresses.txt", "./cheats.txt")



#--------------------SETTINGS--------------------
lpc = 50
offset = "D3000000 10000000"
offsetN = "1"
base = "3F800000"
replaceL = "3F000000"
replaceR = "40000000"
#--------------------SETTINGS--------------------



#Check and stock the number of file lines
print("Opening cheats.txt...")
print("")
nmbrlines = 0
f = open("cheats.txt", 'r')
for line in f:
    nmbrlines += 1
print("You START with", nmbrlines ,"lines")




#Calculates the last lines
nmbrlinesbis = nmbrlines
calclines = 0
while nmbrlinesbis > lpc:
    nmbrlinesbis = nmbrlinesbis - lpc
    calclines = calclines + lpc
linesfin = nmbrlinesbis
print("(",lpc,"*",calclines/lpc,")  +  ->",linesfin,"MORE line(s) <-")




#------------------------------------------------
#-----------DELETE ALL ": " IF PRESENT-----------
#------------------------------------------------



#Replace all the " : " by " "
with open("cheats.txt","r") as f:
    text = f.read().replace(": ","")

with open("cheats.txt", "w") as f:
    f.write(text)


    
#Replace all 1st numbers by "0"
with open("cheats.txt","r") as f:
    text = f.read().replace("\n"+offsetN,"\n0")

with open("cheats.txt", "w") as f:
    f.write(text)



#------------------------------------------------
#------PUT SPACES TO SET LIMITS FOR CHEATS-------
#------------------------------------------------


#Pass 1 line at the last line
with open("cheats.txt","r+") as f:
        text = f.readlines()
        text.insert(nmbrlines,"\n")
        f.seek(0)
        f.writelines(text)

#Pass 1 line at the first line
with open("cheats.txt","r+") as f:
        text = f.readlines()
        text.insert(0,"\n")
        f.seek(0)
        f.writelines(text)



#Def the LIMITATIONS
limitation = (calclines/lpc)
print("Limitation =",limitation)



#Set some values
it = 0
serie = 0
fix = 0

#Jump 2 lines every (lpc) lines
while limitation > it:
    with open("cheats.txt","r+") as f:
        text = f.readlines()
        text.insert(lpc+1+(serie*(lpc+fix)),"\n\n")
        f.seek(0)
        f.writelines(text)
    it = it + 1
    serie = serie + 1
    fix = 2



#------------------------------------------------
#------------ADD NAME FOR ALL CHEATS-------------
#------------------------------------------------



it = 0
step = 0


#Mark [* Step] for each packages
while limitation >= step :
    with open("cheats.txt","r+") as f:
        steptext = f"[{step + 1} Step]\n"+offset
        text = f.readlines()
        text.insert((lpc + 3) * step,steptext)
        f.seek(0)
        f.writelines(text)
    step = step + 1



#------------------------------------------------
#---------------ADD "IF" FUNCTIONS---------------
#------------------------------------------------



it = 0
serie = 0
fix = 0


#Add code at all the (lpc) lines
while limitation > it:
    with open("cheats.txt","r+") as f:
        text = f.readlines()
        text.insert(lpc+fix+2+(serie*lpc),"DD000000 00000200\n\nD0000000 00000000\nDD000000 00000100\n\nD0000000 00000000\n")
        f.seek(0)
        f.writelines(text)
    it = it + 1
    serie = serie + 1
    fix = fix + 9


with open("cheats.txt","r+") as f:
    text = f.readlines()
    text.insert(linesfin+fix+2+(serie*lpc),"DD000000 00000200\n\nD0000000 00000000\nDD000000 00000100\n\nD0000000 00000000\n")
    f.seek(0)
    f.writelines(text)



#------------------------------------------------
#----------COPY ADRESSES IN "IF" PARTS-----------
#------------------------------------------------



it = 0
serie = 0



#Copy lpc adresses in some places (1/2)
while limitation > it:
    with open("cheats.txt","r+") as f:
        text = f.readlines()
        addr = text[:(serie * (7 + (lpc*3))) + lpc + 3]    +    text[(serie * (7 + (lpc*3))) + 2:(serie * (7 + (lpc*3))) + lpc + 2]    +    text[(serie * (7 + (lpc*3))) + lpc + 4:(serie * (7 + (lpc*3))) + lpc + 6]    +    text[(serie * (7 + (lpc*3))) + 2:(serie * (7 + (lpc*3))) + lpc + 2]    +    text[(serie * (7 + (lpc*3))) + lpc + 7:]
        f.seek(0)
        f.write("".join(addr))
    it = it + 1
    serie = serie + 1




#Copy lpc adresses in some places (2/2)
with open("cheats.txt","r+") as f:
    text = f.readlines()
    addr = text[:(serie * (7 + (lpc*3))) + linesfin + 3]    +    text[(serie * (7 + (lpc*3))) + 2:(serie * (7 + (lpc*3))) + linesfin + 2]    +    text[(serie * (7 + (lpc*3))) + linesfin + 4:(serie * (7 + (lpc*3))) + linesfin + 6]    +    text[(serie * (7 + (lpc*3))) + 2:(serie * (7 + (lpc*3))) + linesfin + 2]    +    text[(serie * (7 + (lpc*3))) + linesfin + 7:]
    f.seek(0)
    f.write("".join(addr))



#------------------------------------------------
#-------------SET VALUES FOR BUTTONS-------------
#------------------------------------------------



it = 0
serie = 0


#Replace all the "base" by "replaceL" for L (1/2)
while limitation > it:
    with open("cheats.txt", "r") as f:
        linesL = f.readlines()

    with open("cheats.txt", "w") as f:
        for i in range(((serie * (7 + (lpc * 3))) + lpc + 3)   ,   ((serie * (7 + (lpc * 3))) + (lpc * 2) + 3)):
            linesL[i] = linesL[i].replace(base, replaceL)
        f.write("".join(linesL))
    it = it + 1
    serie = serie + 1




#Replace all the "base" by "replaceL" for L (2/2)
with open("cheats.txt", "r") as f:
    linesL = f.readlines()

with open("cheats.txt", "w") as f:
    for i in range(((serie * (7 + (lpc * 3))) + linesfin + 3)   ,   ((serie * (7 + (lpc * 3))) + (linesfin * 2) + 5)):
        linesL[i] = linesL[i].replace(base, replaceL)
    f.write("".join(linesL))





it = 0
serie = 0



#Replace all the "base" by "replaceR" for R (1/2)
while limitation > it:
    with open("cheats.txt", "r") as f:
        linesR = f.readlines()

    with open("cheats.txt", "w") as f:
        for i in range(((serie * (7 + (lpc * 3))) + (lpc * 2) + 3)   ,   ((serie * (7 + (lpc * 3))) + (lpc * 3) + 5)):
            linesR[i] = linesR[i].replace(base, replaceR)
        f.write("".join(linesR))
    it = it + 1
    serie = serie + 1




#Replace all the "base" by "replaceR" for R (2/2)
with open("cheats.txt", "r") as f:
    linesR = f.readlines()

with open("cheats.txt", "w") as f:
    for i in range(((serie * (7 + (lpc * 3))) + (linesfin * 2) + 3)   ,   ((serie * (7 + (lpc * 3))) + (linesfin * 3) + 5)):
        linesR[i] = linesR[i].replace(base, replaceR)
    f.write("".join(linesR))




#------------------------------------------------
#-!!!!!!!!!!!!!!!-END OF PROGRAM-!!!!!!!!!!!!!!!-
#------------------------------------------------


#Regive the number of lines
nmbrlines = 0
f = open("cheats.txt", 'r')
for line in f:
    nmbrlines += 1
print("You FINISH with", nmbrlines ,"lines")
print("")
f.close()
