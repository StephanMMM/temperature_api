from . import schemas

def convert_temperature(temperature: schemas.TemperatureConvert):
    if temperature.new_unit == "fahrenheit" and temperature.unit != "fahrenheit":
        return _convert_to_fahrenheit(temperature)
    if temperature.new_unit == "celsius" and temperature.unit != "celsius":
        return _convert_to_celsius(temperature)

def _convert_to_fahrenheit(temperature: schemas.TemperatureBase):
    if temperature.unit == "celsius":
        return schemas.TemperatureBase(degrees=(temperature.degrees*9/5) + 32,
                                       unit="fahrenheit")

def _convert_to_celsius(temperature: schemas.TemperatureBase):
    if temperature.unit == "fahrenheit":
        return schemas.TemperatureBase(degrees=(temperature.degrees - 32) * 5 / 9,
                                       unit="celsius")