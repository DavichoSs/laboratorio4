archivo=open('texto.txt','r')
contenido=archivo.readline()
b=contenido.replace(" ","")
c=len(b)
print("Numero de letras: "+str(c))