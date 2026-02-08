import os
f = open("inf.txt", "w")

f.write(str(os.stat(os.listdir()[0])))