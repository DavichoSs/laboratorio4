from textblob import TextBlob

textp1= '''
La historia empieza cuando Harry es dejado en la casa de sus Tios, los Dursley, por Rubeus Hagrid, Albus Dumbledore y Minerva McGonnagall. 
Alli mencionan que Lord Voldemort, el mago mas tenebroso de esos tiempos habia sido vencido, luego de intentar matar a Harry Potter. Harry sobrevivio a la maldicion asesina, con no otra secuela que una cicatriz con forma de rayo en la frente. Como consecuencia de los actos de Voldemort, los padres de Harry, Lily y James, habian muerto, y por eso Harry debia quedarse con sus tios. ni
El libro continua diez anios despues, donde vemos que Harry no es nada feliz con sus tios, ni sabe que es mago. Los Dursley malcrian a su hijo Dudley, mientras que a Harry lo tratan como un sirviente. 
Harry sospecha que es especial, y mas cuando en el cumpleanios de Dudley, en un zoologico, hace desaparecer un cristal, haciendo caer a su primo en la jaula de una Boa Constrictora. 
Poco antes de su cumpleanios Harry recibe una carta de Hogwarts, pero no logra abrirla o causa de su tio, que no quiere que el chico se entere de que puede hacer magia. Los esfuerzos de Vernon no prosperan, y siguen llegando cartas, traidas extraniamente por lechuzas. Para que no haya mas disturbios con las cartas, la familia Dursley con Harry se mudan a una casita en una islita. 
El dia de cumpleanios de Harry, todavia en esa casita, llega el gigantesco Hagrid a entregarle la carta personalmente, y a desearle feliz cumpleanios. Vernon se tiene que dar por vencido, y Harry se entera de toda la verdad. 
La carta decia que Harry estaba invitado a participar del primer anio en el Colegio Hogwarts de Magia y Hechizeria. Harry se entusiasma por salir de su vida como muggle, de escaparse de los Dursley, a un lugar donde todos serian como el. 
Hagrid lleva a Harry al Callejon Diagon a comprar sus cosas para el colegio. Harry, con el Guardian de Llaves de Hogwarts, va al banco de los magos, Gringotts, donde descubre que sus padres le habian dejado una gran fortuna. Luego, por “asuntos de Hogwarts” van a la camara 713 y Hagrid se lleva un paquete misterioso… Harry compra una varita, libros, y Hagrid le regala a Hedwig, una lechuza. 
Luego empieza el anio en Hogwarts. 
Al llegar Harry descubre que hay cuatro casas; Gryffindor, Slytherin, Ravenclaw y Hufflepuff, y que va a ser asignador a una. Ron Weasley, un chico que habia conocido en el tren que los llevaba al Colegio, le dice que en Slytherin estaban los magos malos, y Harry desea no entrar a esa casa. Finalmente termina con Ronald en Gryffindor, y el que acaba en Slytherin es Draco Malfoy, un chico que habia insultado a Ron. El director de Hogwarts, Dumbledore, dice que ese anio no se iba a poder entrar en un cuarto del tercer piso. Alli cursa materias antes desconocidas para el, como Pociones, con el Profesor Snape, Defensa Contra las Artes Oscuras, con el Profesor Quirrell, Encantamientos, Transformaciones, y otras mas. Harry conoce a Ron Weasley, y se hacen muy amigos. Luego de vencer a un troll en Halloween, Harry se hace otra mejor amiga; Hermione Granger. 
En Navidad, Harry recibe anonimamente una capa invisible, que oculta a la vista de los demas al que la usa. Una nota dice que era de su padre, y que la utilice bien.
'''

en_blob = TextBlob(textp1)
en_blob.translate(to='en')