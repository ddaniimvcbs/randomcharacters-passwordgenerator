*ADVERTENCIA* Al haber usado el modulo "random", estas contraseñas os recomiendo utilizarlas para redes sociales y poco mas. Su algoritmo (Mersenne Twister) es predecible. Sin embargo, se puede usar el modulo "secrets" (haré un generador con ese modulo en especifico mas adelante) que sí serian mas seguras.


En primer lugar, gracias por echarle un simple vistazo a esto, tal vez te pueda ayudar a aprender algo de Python, si es asi me alegro. Soy muy nuevo en esto de la programacion, pero os detallare el porque del todo el codigo aqui, para así tambien poder ver si estoy entendiendo lo que estoy programando.

Las contraseñas a dia de hoy, son una parte fundamental de la proteccion de nuestras credenciales. Aunque existen metodos como el 2FA, etc.. siempre debemos asegurarnos de que nadie puede saber, ni adivinar, por fuerza bruta (a no ser que os infecten con un InfoStealer...) nuestra contraseña.

ACLARO QUE EL CODIGO PUEDE BUGUEARSE, POR EJEMPLO, INTRODUCCIENDO UNA LETRA DONDE SE GUARDA LA VARIABLE DEL INPUT PARA PARA LA LONGITUD DE LA CONTRASEÑA, CONFORME VAYA APRENDIENDO EXCEPCIONES DE ERRORES, DEPURACION, ETC.. LO IRÉ ARREGLANDO..




INTRODUCCION AL CODIGO:
¿Como se llega a crear esto?

Primero, vamos a definir una simple funcióon, sin parametros. (Actualmente, estoy aprendiendo esto justamente en Python)

¿Por que sin parametros?

No nos hacen falta. Punto. Aunque aclaro que por ejemplo, podria poner que trabajara con el parametro "lista", por ejemplo..

Por logica pura, tenemos que añadir, o bien una tupla entera con todos los numeros,letras y simbolos, o hacer 3 tuplas con numeros, letras,simbolos. He decidido hacerlo asi para jugar con "zip" y otras cosillas.

Tambien podemos no utilizar tuplas y solo strings, cada uno tiene su idea.

Bien, ahora decidí que hay que darle un límite a los caracteres generados, si solo quieres una contraseña de 25, pues de 25, y viceversa.

*ATENCION*--- Si pones un numero MUY ELEVADO de caracteres(algo como 3948729047289) Python explotará.

Como soy nuevo, solo puedo deducir esto sin probarlo en el script, no me hace falta ya que tampoco es muy dificil de pensarlo.

Debemos crear la variable "longitud" que es donde guardaremos el numero que le pidamos al usuario para su limite de caracteres de la contraseña. Debemos poner int(input), ya que el usuario colocara un numero entero, y bueno, obviamente si ponemos solo input(), Python tratará el dato como un data type strings (un poquito de nivel de ingles, haber si mejoramos tambien...).

Una vez hecho esto, ya recogeremos el numero maximo de caracteres para la contraseña del usuario

Ahora, en mi caso, al tener la lista partida en 3, he creado una variable que agrupe las 3 variables en una sola string  (todos_los_caracteres = numeros + letras + simbolos)

Bien, ahora haremos uso de unos de los primeros modulos, junto con time y maths, que aprendí, random.

Os recomiendo este modulo para ir jugando con ellas como primer contacto.

Pues obviamente, tenemos que crear otra variable donde recoja la accion que le daremos a la libreria:

contraseña = random.choices(todos_los_caracteres, k=longitud)

Aqui es donde se genera la "magia" (la funcion empieza a hacer funciones, jaja...(risas))

random.choices nos permite cojer elementos de la lista unica que hemos creado con todos_los_caracteres y generar, la contraseña.

Pero.. ¿de donde viene k=longitud?

Bien hecho..ahora no sabes ni de donde viene "longitud",¿verdad?

Recordando, habiamos creado una variable llamada longitud para recoger el numero maximo de caracteres para la contraseña..¿verdad? ¿te acuerdas?. Eso espero..

Si no fijasemos una variable con la longitud, y k fuera = 5, la contraseña seria de 5 CARACTERES. k = define cuantos caracteres van a generarse de la lista completa, por eso, si el usuario no es el que fija el numero, el script va a generar por ejemplo, todo el rato, una contraseña de 10,15,20 caracteres.



Bien.. pues ya tenemos el resultado de la contraseña, ahora hacemos otra variable para guardar la contraseña generada y print...

Vamos a ejecutar el print, vamos a hacer una de 10 caracteres..

['_', 'b', 'b', '&', '|', '_', 'j', 'b', 'e', 'j']

Si muchacho, eso es una aberracion, vaya output mas feo..

¿Lo arreglamos?

""join. tiene una mision muy facil, convertir varios elementos de listas,tuplas,etc.. a una sola string.


Pues sencillo, hacemos otra variable "contraseña_lista" y listo.

Por ultimo hacemos un print final...

Contraseña lista!

Este es el flujo explicado de mi primer script, espero que os guste!!!!.



















