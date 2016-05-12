def creartxt():
    archivo=open('datos.txt','w')
    archivo.close()
 
def grabartxt():
    archivo=open('datos.txt','a')
    archivo.write('Hola mundo\n')
    archivo.write('Mi nombre es Alexander\n')
    archivo.write('Mi compa se llama Ruben\n')
    archivo.close()
 
creartxt()
grabartxt()
