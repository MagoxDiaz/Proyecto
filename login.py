import os

if __name__ == '__main__':  
    print(" {:^50} {:^50} {:^50} ".format('', 'INGRESAR', '')) #Formato para colocar 3 casillas con espacios de 50, para que así el titulo quede en el centro, los ^ hacen la función
    #codigo para pedir el nombre de usuario y contraseña
    print ("Username:   ") 
    n = input("  ")
    print ("Contraseña:   ") 
    c = input("  ") 
    
    #Username y contraseña que admite el programa para iniciar sesión 
    if n == "juan":
        if c == "1234": 
           print ("CORRECTO") 
           os.system('cls')
           print ("Bienvenido administrador")
    elif n == "Magox":
        if c == "havanna":
            print ("CORRECTO") 
            os.system('cls') #Limpiar pantalla
            ("Bienvenido usuario") 
    elif n =="luzz": 
        if c == "yolol": 
            print ("CORRETO")
            os.system('cls') 
            print ("Bienvenido administrador")
    else:
        print ("INCORRECTO") 
        
    