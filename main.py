from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Servidor ejecutandose"}

usuarios = [
    {
        'id': 1,
        'username': 'Reinel',
        'password': 'quiz'
    },
    {
        'id': 2,
        'username': 'James',
        'password': 'jajaja'
    },
    {
        'id': 3,
        'username': 'Johan',
        'password': 'pina'
    },
    {
        'id': 4,
        'username': 'Camilo',
        'password': '1234'
    },
    {
        'id': 5,
        'username': 'chatgpt',
        'password': 'version4'
    }
]

@app.get("/user/all/")
def listar_allUsers():
    return usuarios

@app.get("/user/unique/{id_usuario}")
def listar_justOne(id_usuario:int):
    #buscar el usuario en la lista
    for user in usuarios:
        if user['id'] == id_usuario:
            return user
    return {"message": "No se encontro el usuario en la base de datos"}

class User(BaseModel):
    username: str
    id:int
    password:str

@app.post("/user/addusr/")
def add_usr(user:User):
    #id username password

    for usuario in usuarios:
        if user.username == usuario['username']:
            return {"message": "Usuario ya existe"}
    
    #metodo para agregar en la base de datos
    usuarios.append(user)
    return {"message": "Usuario añadido con exito"}