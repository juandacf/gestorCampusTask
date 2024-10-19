import login as l

def createBoard(mainDict, user):
    for k,v in mainDict.items():
        if v.get('userName')== user:
            userIndex= k
    boardName= str(input("Por favor, ingrese el nombre de su tablero: "))
    
    mainDict.get(userIndex).get('boards')

    