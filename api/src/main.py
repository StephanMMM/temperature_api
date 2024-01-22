from fastapi import Depends, FastAPI, HTTPException

from . import operations, schemas

VALID_UNITS = {
    "celsius",
    "fahrenheit"
}

api = FastAPI()


@api.post("/temperature/convert", response_model=schemas.TemperatureBase)
async def convert_temperature(temperature: schemas.TemperatureConvert):
    if temperature.new_unit not in VALID_UNITS \
            or temperature.unit not in VALID_UNITS \
            or temperature.new_unit == temperature.unit:
        raise HTTPException(status_code=404, detail="Temperature unit is invalid.")
    converted_temperature = operations.convert_temperature(temperature)
    return converted_temperature
