from os import getenv
import requests
import aiohttp
from fastapi import HTTPException

EXCHANCE_APIKEY = getenv('EXCHANCE_APIKEY')

def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANCE_APIKEY}/pair/{from_currency}/{to_currency}'
    
    try:
        response = requests.get(url=url)

        data = response.json()
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=400, detail=error)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=error)

    if "conversion_rate" not in data:
        raise HTTPException(status_code=400, detail="Conversion rate not in response")
    
    try:
        exchange_rate = float(data['conversion_rate'])
    except (KeyError, ValueError) as error:
        raise HTTPException(status_code=400, detail=f"Error extracting exchange rate: {error}")

    converted_price = price * exchange_rate
    
    return {'converted_price': converted_price}
    


async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANCE_APIKEY}/pair/{from_currency}/{to_currency}'
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
             data = await response.json()
             
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=400, detail=error)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=error)

    if "conversion_rate" not in data:
        raise HTTPException(status_code=400, detail="Conversion rate not in response")
    
    try:
        exchange_rate = float(data['conversion_rate'])
    except (KeyError, ValueError) as error:
        raise HTTPException(status_code=400, detail=f"Error extracting exchange rate: {error}")
    
    return {to_currency: price * exchange_rate}