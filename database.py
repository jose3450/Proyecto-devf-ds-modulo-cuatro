from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://devfProjectTest:ZJhN7VykwQyw2cMn@apidevfprojectcluster.1ph4bgt.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFILE = ca)
        db = client["proyectoDevfModuloCuatroJZ"]
    except ConnectionError:
        print("Error de Conexión con la base de datos.")
    return db
