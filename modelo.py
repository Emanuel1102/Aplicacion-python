from pymongo import MongoClient
import certifi

urlMongo="mongodb+srv://emanuel:mongo1802@cluster0.dqjgpat.mongodb.net/?retryWrites=true&w=majority"
ca=certifi.where()

def conexionBd():
    try:
        client=MongoClient(urlMongo, tlsCAFile=ca)
        bd=client["Registro_de_usuarios"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return bd