def createUser (mainDict):
    userName= str(input("Por favor, inserte su nombre de usuario")) 
    password= str(input("Por favor, ingrese su contraseña"))

    constructor= {
        'userName': userName,
        'password': password,
        'lists': {

        }
    }

    for k,v in mainDict.items():
        if v.get('userName')== userName:
            input("Este nombre de usuario ya existe. Por favor, oprima enter e intente con otro. ")
        else:
            mainDict.update({len(mainDict)+1: constructor})

def logIn (mainDict):
    userName= str(input("Por favor, ingrese su nombre de usuario"))
    password= str(input("Por favor, ingrese su contraseña"))
    validationSwitch = False

    for k,v in mainDict.items():
        if v.get('userName')== userName:
            if v.get('password')== password:
                validationSwitch = True
    
    if (validationSwitch==True):
        return userName
    else:
        return False




