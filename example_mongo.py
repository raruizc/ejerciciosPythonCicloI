from pymongo import MongoClient

mongoClient = MongoClient('127.0.0.1', port = 27017)

print(mongoClient.list_database_names())

variable_db = mongoClient.restaurante # Crear base de datos 
#print(variable_db)
coleccion_producto = variable_db.producto # Crear colección

#dict_1 = {"nombre": "Partido", "polla":"perdieron"}
#id_ = coleccion_producto.insert_one(dict_1)
#print(id_.inserted_id)


for elemento in coleccion_producto.find():
    print(elemento)
    #coleccion_producto.remove() 
    #print("\n", elemento)

  