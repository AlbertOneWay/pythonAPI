import sys
sys.path.append("..") 

from fastapi import APIRouter
from schemas import User
from database import USUARIOS

user = APIRouter()

@user.get("/all/")
def listar_allUsers():
    return USUARIOS

@user.get("/unique/{id_usuario}")
def listar_justOne(id_usuario:int):
    #buscar el usuario en la lista
    for user in USUARIOS:
        if user['id'] == id_usuario:
            return user
    return {"message": "No se encontro el usuario en la base de datos"}

@user.post("/addusr/")
def add_usr(user:User):
    #id username password

    for usuario in USUARIOS:
        if user.username == usuario['username']:
            return {"message": "Usuario ya existe"}
    
    #metodo para agregar en la base de datos
    USUARIOS.append(user)
    return {"message": "Usuario añadido con exito"}

@user.post("/login/")
def login(user:User):
    for usuario in USUARIOS:
        if (user.username == usuario['username']) and (user.password == usuario['password']):
            return{"message": "Acceso correcto",
                   "token": "ADIDCXC6T"}
    return{"message": "Verifique sus credenciales"}
            