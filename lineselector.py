#Compare "cheats1.txt" and "cheats2.txt"
#Write all lines which are present in the 2 files in "cheatequal.txt"

import shutil

with open("cheats1.txt","r+") as f, open("cheats2.txt","r+") as g:


    nmbrlines = 0
    fline = open("cheats1.txt", 'r')
    for line in fline:
        nmbrlines += 1
    print("onetxt have", nmbrlines ,"lines")
    fline = nmbrlines

    nmbrlines = 0
    gline = open("cheats2.txt", 'r')
    for line in gline:
        nmbrlines += 1
    print("twotxt have", nmbrlines ,"lines")
    gline = nmbrlines
    n = "\n"
    n = list(n)


f.close
g.close


#---------------------------------------------------------


shutil.copy("cheats1.txt", "cheats1temp.txt")
shutil.copy("cheats2.txt", "cheats2temp.txt")

f = open("cheats1.txt","r+")
g = open("cheats2.txt","r+")
h = open("cheats1temp.txt","r+")
i = open("cheats2temp.txt","r+")

factualine = 1
gactualine = 1
fall = f.readlines()
gall = g.readlines()


timeout = 0
while nmbrlines > timeout:
    i.seek(0)
    firsttxt = h.readline()
    secondtxt = i.readline()

    it = 0
    found = 0

    while it < nmbrlines:
        if firsttxt == secondtxt:
            gall = gall[:gactualine - 1] + gall[gactualine:]
            it = nmbrlines
            found = 1
        else:
            gactualine = gactualine + 1
            secondtxt = i.readline()
            it = it + 1

    if found == 0:
        fall = fall[:factualine - 1] + fall[factualine:]
        print("Not same")
    else:
        factualine = factualine + 1
        print("Same")
    timeout = timeout + 1
    print("Timeout = ",timeout,"/",nmbrlines)

with open("cheatequal.txt","w") as j:
    j.write("".join(fall))

f.close()
g.close()
h.close()
i.close()
j.close()