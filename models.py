from typing import Union
from pydantic import BaseModel

class Partido(BaseModel):
    anyo: int
    fase: Union[str, None] = None
    equipolocal: Union[str, None] = None
    goleslocales: Union[int, None] = None
    golesvisitante: Union[int, None] = None
    equipovisitante: Union[str, None] = None
    estaequipoanfitrion: Union[int, None] = None