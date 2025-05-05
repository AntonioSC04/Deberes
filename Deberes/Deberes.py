from Funciones import get_deberes, write_deberes
import time

today = time.strftime("%B %d, %Y %H:%M:%S") #Importo el modulo de tiempo para imprimir la fecha y hora del dia de hoy
print(today)

while True:
    user_action = input("Agrega un deber, editalo, completalo, visualizalo o sal del programa: ")
    
    if user_action.startswith("add"):
            deber = user_action[4:].capitalize() + "\n"
            
            deberes = get_deberes() #Reemplazo el codigo de la lectura del archivo por el metodo get_deberes
                 
            deberes.append(deber)
            
            write_deberes(deberes)
        
    elif user_action.startswith("show"):

            deberes = get_deberes()

            for index, item in enumerate(deberes):
                item = item.strip('\n') #Elimina los espacios extra entre cada deber mostrado
                index = index + 1
                print(f"{index}. {item.capitalize()}")

    elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                number = number - 1

                deberes = get_deberes()

                nuevo_deber = input("Ingresa el nuevo deber: ")
                deberes[number] = nuevo_deber + '\n'

                write_deberes(deberes)

            except ValueError:
                 print("Tu comando no es valido")
                 continue

    elif user_action.startswith("complete"):
            try:
                number = int(user_action[9:])

                deberes = get_deberes()

                index = number - 1
                removido = deberes[index]
                deberes.pop(index)

                write_deberes(deberes)

                message = f"El deber: {removido.strip()}, ha sido removido de la lista"
                print(message)
            except IndexError:
                 print("El numero de la lista ingresado a completar no existe")
                 continue


    elif user_action.startswith("exit")in user_action:
        break

    else:
         print("Ingresaste un comando invalido")    
    

print("Bye")
            


