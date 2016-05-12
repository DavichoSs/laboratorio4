z=0
a=int(input("Cuantas frases desea ingresar: "))
for i in range(1,a+1):
	cadena=input("Ingrese frase "+str(i)+" :")
	b=cadena.replace(" ","")
	c=len(b)
	z=z+c
	print("Existen: "+str(len(b))+" letras.")
print("Total de caracteres: "+str(z))