from httpx import AsyncClient

from src.core.config import KEY_API_CURRENTS


async def calculate_converted(_from: str, _to: str, volume: int):
    """
    Подсчёт ответа на запрос.
    :param _from: Валюта из которой переводим.
    :param _to: Валюта, в которую нужно конвертировать.
    :param volume: Количество для конвертации.
    """
    date_update, price = await get_data_to_api_coin_market(
        currency=_from, new_currency=_to
    )
    all_price = round(price * volume, 3)

    return date_update, all_price


async def get_data_to_api_coin_market(
    currency: str,
    new_currency: str,
) -> tuple:
    """
    Получение данных о валютах по API app.currencyapi.com.
    :param currency: Валюта из которой переводим.
    :param new_currency: Валюта, в которую нужно конвертировать.
    """

    url_request = (f"https://api.currencyapi.com/v3/latest?"
                   f"apikey={KEY_API_CURRENTS}&"
                   f"currencies={new_currency}&"
                   f"base_currency={currency}")

    async with AsyncClient() as client:
        response = await client.get(url_request)
        response.raise_for_status()

    data = response.json()
    date_update = data["meta"]["last_updated_at"]
    price = data["data"][new_currency]["value"]

    return date_update, price
