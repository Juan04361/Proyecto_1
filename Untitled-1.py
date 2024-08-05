while True:
    print("Selecciona una opcion:")#Inicio.
    print("1. Para sumar") #Opcion para suma.
    print("2. Para multiplicar") #Opcion para multiplicacion.
    print("3. Para dividir") #Opcion para dividir.
    print("4. Para restar") #Opcion para restar.
    print("5. Para calcular la raiz cuadrada") #Opcion para raiz cuadrada.
    print("6. Salir de la calculadora") #Opcion para salir.
 
    opcion = input("Ingrese opcion: ") #El usuario ingresa la opcion que quiera.
    if opcion == "1": #Para suma.
       numero1 = float(input("Ingrese el primer numero: ")) #Ingrese num1.
       numero2 = float(input("Ingrese el segundo numero: ")) #Ingrese num2.
       resultado = numero1 + numero2 #Se obtiene el resultado por medio de la suma.
       print(resultado) #Se imrprime en la pantalla el resultado de la suma.
    elif opcion == "2": #Para multiplicar.
       numero1 = float(input("Ingrese el primer numero: ")) #Ingrese num1.
       numero2 = float(input("Ingrese el segundo numero: ")) #Ingrese num2.
       resultado = numero1 * numero2 #Se obtiene el resultado por medio de la multiplicacion.
       print(resultado) #Se imrprime en la pantalla el resultado de la multiplicacion.
    elif  opcion == "3": #Para dividir.
       numero1 = float(input("Ingrese el primer numero: ")) #Ingrese num1.
       numero2 = float(input("Ingrese el segundo numero: ")) #Ingrese num2.
       resultado = numero1 / numero2 #Se obtiene el resultado por medio de la division.
       print(resultado) #Se imrprime en la pantalla el resultado de la division.
    elif opcion == "4": #Para restar.
       numero1 = float(input("Ingrese el primer numero: ")) #Ingrese num1.
       numero2 = float(input("Ingrese el segundo numero: ")) #Ingrese num2.
       resultado = numero1 - numero2 #Se obtiene el resultado por medio de la resta.
       print(resultado) #Se imrprime en la pantalla el resultado de la resta.
    elif opcion == "5": #Para calcular la raiz cuadrada.
       import math #El módulo math proporciona funciones y constantes para poder realizar operaciones más avanzadas.

       numero = float(input("Ingresa un numero para calcular su raiz cuadrada: ")) #Ingrese num.
       raiz_cuadrada = math.sqrt(numero) #Se obtiene el resultado de la raiz cuadrada.
       print("La raiz cuadrada de", numero, "es:", raiz_cuadrada) #se imrprime en la pantalla el resultado de la raiz cuadrada.
    elif opcion == "6": #Para salir.
       print("Ha decidido salir") #Se imrprime en la pantalla el mesaje: "Ha decidido salir".
       break #Salir.
    else: #Indica que la opcion es falsa.
       print("Opcion no valida.") #Es el mensaje que nos indica que no existe la opcion indicada.