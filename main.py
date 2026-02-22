from typing import Union, Annotated
from fastapi import FastAPI, Response, status, Body
from docs import tags_metadata
from futboldata import FutbolData
from models import Partido

# Objeto para trabajr con los datos de los partidos
futbol = FutbolData()

# Objeto app de tipo FastAPI
app = FastAPI(
    title="Futbol API",
    description="ApiRestful para datos de futbol",
    version="0.0.1",
    openapi_tags=tags_metadata
)

# Creamos endpoints

# Default
@app.get("/")
def read_root():
    return {"Hola": "root"}

# Get partidos o todos los partidos
@app.get("/partidos", tags=["partidos"])
async def read_partidos(total: int, skip: int=0, todos: Union[bool, None]=None):
    if todos:
        return await futbol.get_allIPartidos()
    else:
        return await futbol.get_partidos(skip, total)

# Realmente esta funcion ya cumple con el /partidos de la funcion pasada pero igual lo pide
@app.get("/todospartidos", tags=["partidos"])
async def read_todos_partidos():
    return await futbol.get_allIPartidos()

# Get partidos en un equipo
@app.get("/partidosequipo", tags=["partidos"])
async def read_partidos_equipos(equipo: str):
    return await futbol.get_partidosEquipo(equipo)

# Get un partido
@app.get("/partidos/{partido_id}", tags=["partidos"], status_code=status.HTTP_200_OK)
async def read_partido(partido_id: int, response: Response):
    existe_partido = await futbol.get_partido(partido_id)
    if existe_partido:
        return existe_partido
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(partido_id)+" no encontrado"}
    
# Post partido
@app.post("/partidos", tags=["partidos"])
async def write_partidos(partido: Partido):
    return await futbol.write_partido(partido)

# Update partido
@app.put("/partidos/{partido_id}", tags=["partidos"], status_code=status.HTTP_200_OK)
async def update_partido(partido_id: int, partido: Partido, response: Response):
    existe_partido = await futbol.get_partido(partido_id)
    if existe_partido:
        return await futbol.update_partido(partido_id, partido)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(partido_id)+" no encontrado"}

# Delete partido
@app.delete("/partidos/{partido_id}", tags=["partidos"], status_code=status.HTTP_200_OK)
async def delete_partido(partido_id: int, response: Response):
    existe_partido = await futbol.get_partido(partido_id)
    if existe_partido:
        return await futbol.delete_partido(partido_id)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(partido_id)+" no encontrado"}
