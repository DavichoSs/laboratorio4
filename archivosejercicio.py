def grabartxt():
    archivo=open('datos.txt','w')
    archivo.write('Hola mundo\n')
    archivo.write('Mi nombre es Alexander\n')
    archivo.write('Mi compa se llama Ruben\n')
    archivo.close()
grabartxt()
