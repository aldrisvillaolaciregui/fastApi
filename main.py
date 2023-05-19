from fastapi import FastAPI
from sqlite import database
from sqlite import recordatorio
from schemas import recordatorioModel


app = FastAPI()
 
#correr el servidor py -m uvicorn main:app --reload 
@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()
    database.table_exists([recordatorio])
        
@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close() 
    

@app.get('/')
def index():
    return('hola mundo')

@app.get('recordatorio')
def read_recordatorio(recoradorio: recordatorioModel):
    return ('leyendo un recordatorio')


