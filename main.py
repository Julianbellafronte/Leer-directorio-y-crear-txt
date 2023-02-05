from os import listdir


file = open("canciones.txt", "w")
for cosa in listdir(r"C:\Users\julia\Desktop\Progre"):
    file.write('\n'+cosa.split(".")[0].replace("-"," "))
file.close()
    