cantidad_medicos = 0
especialista_senior = 0
residente_junior = 0


while True:
    print("Bienvenido al sistema de registro de médicos, Hospital Central Metropolitano")
    try:
        cantidad_medicos = int(input("Ingrese la cantidad de médicos a registrar: "))
        if cantidad_medicos <= 0:
            print ("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
        else: 
            print ("Se han registrado", cantidad_medicos, "médicos")
            break
    except ValueError:
        print ("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
        
for i in range (cantidad_medicos):
    print ("\nIngresando el médico", (i+1))
    
    while True:
        alias = input("Ingrese el nombre del profesional (min. 6 caracteres, sin espacio):").strip()
        if (len(alias) <6) or (' ' in alias):
            print ("El nombre del profesional debe tener al menos 6 caracteres y no tener espacios en blanco")
        else:
            break
    
    while True:
        try:
            experiencia = int(input("Ingrese su experiencia clínica en años: "))
            if experiencia < 0:
                print ("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            else:
                if experiencia >= 5:
                    especialista_senior = especialista_senior + 1
                    print ("El médico registrado es un especialista senior.")
                else:
                    residente_junior = residente_junior + 1
                    print ("El médico registrado es un residente junior.")
                break 
        except ValueError:
            print ("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        
print ("\nEl hospital cuenta con ", especialista_senior, "especialistas senior y", residente_junior, "residentes junior! ¡Sistema listo para operar!")
    
