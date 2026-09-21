from pydantic import BaseModel, Field


class ServidorPolicialData(BaseModel):
    nombre: str = Field(min_length=3)
    identificacion: str = Field(min_length=2)
    grado: str = Field(min_length=3)
    estado: str = Field(min_length=3)