from pydantic import BaseModel

class TemperatureBase(BaseModel):
    degrees: float
    unit: str

class TemperatureConvert(TemperatureBase):
    new_unit: str