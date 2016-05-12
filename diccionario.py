def crearTxt():
	archivo=open('NumerosTelefonicos.txt','w')
	archivo.close()

crearTxt()

a=int(input("Cuantos contactos desea ingresar a la guia telefonica? "))
i=0
print("\n")
while i<a:
	i+=1
	archivo=open('NumerosTelefonicos.txt','a')
	nombre=input("Ingresa el nombre # "+str(i)+" :")
	telefono=input("Ingresa el telefono del contacto # "+str(i)+" :")
	print("\n")
	archivo.write(str(nombre)+" "+str(telefono)+"\n")
	archivo.close()
pass

