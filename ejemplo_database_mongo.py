from pymongo import MongoClient
from pprint import pprint

verdad = False
mongoClient = MongoClient('127.0.0.1', port = 27017)

miDB = mongoClient.biblioteca # Creación de base de datos
print(miDB)

miCol = miDB.libros # Creación Colección

misLibros = {
    "_id" : 2,
    "autor" : "Gabriel Garcia",
    "titulo" : "Cien Años",
    "año" : 1982,
    "editorial" : "norma",
    "genero" : "Novela"
}

for elemento in miCol.find():
    if elemento["_id"] == misLibros["_id"]:
        print("El id ya se encuentra en la base de datos")
        verdad = False
        break
    else:
        verdad = True
if verdad == True:
    try:
        insertado = miCol.insert_one(misLibros) #insertado
        print(insertado.inserted_id)        
    except Exception as e:
        print(type(e), e)
       
for elemento in miCol.find():
        pprint(elemento)

'''else:
    insertado = miCol.insert_one(misLibros) #insertado
    print(insertado.inserted_id)

    for elemento in miCol.find():
        print(elemento)'''