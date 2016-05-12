def grabartxt():
    archivo=open('datos.txt','w')
<<<<<<< HEAD
    archivo.write('Mi nombre es Alexander Mi compa se llama Ruben')
=======
    archivo.write('Hola mundo Mi nombre es Alexander Mi compa se llama Ruben Pozo')
>>>>>>> origin/master
    archivo.close()
grabartxt()

archivo=open('datos.txt','r')
contenido=archivo.readline()
b=contenido.replace(" ","")
c=len(b)
print ("Contenido del archivo:"+ contenido)
print("Numero de letras : "+str(c))