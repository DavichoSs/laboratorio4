a=int(input("Cuantas frases desea ingresar: "))
for i in range(1,a+1):
	cadena=input("Ingrese frase "+str(i)+" :")
	b=cadena.replace(" ","")
	print("Existen: "+str(len(b))+" letras.")