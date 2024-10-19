import json 
import os
PATHWAY= 'data/storage.json'

def addFile():
    with open(PATHWAY, "w") as af:
        json.dump({}, af, indent=4)

def checkFile():
    if(os.path.isfile(PATHWAY)):
        pass
    else:
        addFile()

def readFile():
    with open(PATHWAY, "r") as rf:
        json.load(rf)

def addData(dictName:dict):
    with open(PATHWAY, "w") as ad:
        json.dump(dictName, ad, indent=4 )



