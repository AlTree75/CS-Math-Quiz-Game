# CS-Math-Quiz-Game
1) Lo primero que hago es usar un comando de impresión o la función de impresión y escribir un valor o cadena para dar la bienvenida a los usuarios.
* print("Welcome to the Quiz! ").
2) Luego escribiré una variable para saber si los usuarios van a jugar o no. Así que escribiré playing = y una función de entrada y escribiré una pregunta entre paréntesis.
* playing = input("Do you want to play? ") 
3) Y luego quiero verificar si los usuarios escribieron sí, así que si escribieron no, finalizaré la programación. if playing no es igual a yes. lo que significa que si el usuario escribió una palabra que no es sí o yes, abandonaré la prueba.
* if playing.lower() != "yes":
* quit()
4) Si el usuario escribe sí, le mostraré una oración para comenzar la prueba.
* print("Great! let's play: ")
5) Después de que el usuario ingresó al cuestionario, daré una primera pregunta y abajo escribiré cuál es la respuesta correcta y, si es correcta, mostraré que es correcta y le daré un punto al usuario, si no lo es, se mostrará incorrecta y sin punto . 
* Q1 = input("What does CPU stand for? ")
* if Q1.lower() == "central processing unit":
*     print('Correct! ')
*     score += 1
* else:
*      print("Incorrect!")
6) Haré lo mismo con otras preguntas copiándolas y solo cambiando su número, pregunta y la respuesta correcta.   
7) Después de que los usuarios terminen todas las preguntas que les di, debo darles su resultado o su puntuación en el cuestionario. Así que al final de mi programa Obtuviste puntos del total de puntos.
* print("You got " + str(score) + "/" + "15" + " questions correct")
Si los usuarios acertaron 10 preguntas obtendrán 10/15 y si 13 el resultado será 13/15
