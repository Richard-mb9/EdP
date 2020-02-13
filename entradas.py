def numerosint(msg):   
    numero = input(f'{msg}')
    isnum = numero.isnumeric()

    while isnum == False:
        numero = input('Por favor digite apenas numeros:')
        isnum = numero.isnumeric()
    
    numero = int(numero)
    return numero
   
