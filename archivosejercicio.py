def grabartxt():
    archivo=open('datos.txt','w')
    archivo.write('Hola mundo Mi nombre es Alexander Mi compa se llama Ruben Pozo')
    archivo.close()
grabartxt()

archivo= open('datos.txt','r')
contenido=archivo.readline()
b=contenido.replace(" ","")
c=len(b)
print ("Contenido del archivo:"+ contenido)
print("numero de letras : "+str(c))