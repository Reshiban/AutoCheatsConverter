#CheatSpliter
import shutil


#--------------------SETTINGS--------------------
lpc = 50
cpf = 100
#--------------------SETTINGS--------------------


nmbrlines = 0
f = open("cheats.txt", 'r')
for line in f:
	nmbrlines += 1
print("You START with", nmbrlines ,"lines")
f.close()
	
limitation = (nmbrlines / (7 + (lpc * 3))) / cpf
print("Limitation =",limitation)
	
serie =1
it = 0

while limitation > it:
	cpfile = shutil.copyfile("./cheats.txt", "cheats%s.txt" % serie)
	with open("cheats%s.txt" % serie,"r") as f:
		text = f.readlines()
		print("Serie =",serie,"/",limitation)
		print("and calcul =",(serie * (7 + (lpc*3))) * cpf,"/",nmbrlines)
		addr = text[((serie - 1) * (7 + (lpc*3))) * cpf:(serie * (7 + (lpc*3))) * cpf]
		f.seek(0)
		f.close()
	with open("cheats%s.txt" % serie,"w") as f:
		f.write("".join(addr))
		f.close()
	it = it + 1
	serie = serie + 1
	