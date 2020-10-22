import pymongo
from pymongo import MongoClient
from pprint import pprint
mongoClient = ""

try:
    mongoClient = MongoClient('127.0.0.1', port = 27017)
    miDb = mongoClient.biblioteca #creacion de base de datos
    print(miDb)
    miCol = miDb.libros #creando la colección

    """# Para actualizar un solo registro
    # miCol.update_one({"id":4},{"$set":{"_id":4}})
    # para imprimir todos los registros en la colleción
    # for x in miCol.find():
    #    print(x)
    """

    # Encontrar el ID Maximo, para tener continuación.
    dictID = []
    for x in miCol.find({},{ "_id": 1 }):
        dictID.append(x["_id"])

    for x in miCol.find("_id"):
        pprint(x)
    
    """
    misLibros = {  #creando el documento
        "_id" : max(dictID)+1, #si no se agrega id, se genera uno predeterminado
        "autor" : input("Ingrese el Autor: "),
        "titulo" : input("Ingresa el titulo: "),
        "año" : int(input("Año de publicación: ")),
        "editorial" : input("Ingresa la editorial: "),
        "genero" : input("Ingresa el genero: ")
    }
    """
    # x = miCol.insert_one(misLibros) #agrega el registro a la colección
    # x guarda el id generado
    # print(x.inserted_id)

    #if miCol.find_one({"_id":1}) == None: #determina si ya existe el id 1
    # x = miCol.insert_one(misLibros) #agrega el registro a la colección
    # x = miCol.insert_many(multiLibros) #agrega el registro a la colección
    #    print(x.inserted_id) #imprime el id
    

    




except Exception as e:
    print(type(e),e)



## Datos usados para la base de datos

    """
    multiLibros = [{
                "_id":2,
                "autor":"Haruka Murakami",
                "titulo":"Kafka en la Orilla",
                "año": 1989,
                "editorial":"Santillana",
                "genero":["novela"]
                },
                {"_id":4,
                "autor":"Ted Dekker",
                "titulo":"TR3S",
                "año":2003,
                "editorial":"grupo nelson",
                "genero":["novela","ficcion","suspenso"]
                },
                {
                "_id":5,
                "autor":"Gene Brewer",
                "titulo":"k-PAX",
                "año":1995,
                "editorial":"grupo nelson",
                "genero":["ficcion","drama"]
                },
                {
                "_id":6,
                "autor":"Jonh Katzenbach",
                "titulo":"El psicoanalista",
                "año":2002,
                "editorial":"grupo nelson",
                "genero":["suspenso","ficcion","thriller"]
                }]
        # utilizada para insertar varios documentos, en una sola linea a la colleción desde una lista
    miCol.insert_many(multiLibros)

    # Utilizado para eliminar varios registros.
    miCol.delete_many({"id":{"$gt":3}})

    # Actualizo los libros previos (que no tenian ESTADO, y se lo agrego)
    miCol.update_many({"_id":{"$gt":0}},{"$set":{"Estado":True}})
"""