from pydantic import BaseModel
from typing import Optional


class recordatorioModel(BaseModel):
    descrip:str
    fecha: Optional[str]=None
    producto:str
    