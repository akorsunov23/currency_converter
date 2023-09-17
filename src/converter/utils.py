import asyncio

from src.core.config import KEY_API_CURRENTS
from httpx import AsyncClient


async def calculate_converted(
		_from: str = None,
		_to: str = None,
		volume: int = None
):
	"""
	Подсчёт ответа на запрос.
	:param _from: Валюта из которой переводим.
	:param _to: Валюта, в которую нужно конвертировать.
	:param volume: Количество для конвертации.
	"""
	cur_data = await get_data_to_api_coin_market(
		currency=_from,
		new_currency=_to
	)


async def get_data_to_api_coin_market(
		currency: str,
		new_currency: str,
) -> dict:
	"""
	Получение данных о валютах по API app.currencyapi.com.
	:param currency: Валюта из которой переводим.
	:param new_currency: Валюта, в которую нужно конвертировать.
	"""

	url_request = f"https://api.currencyapi.com/v3/latest?apikey={KEY_API_CURRENTS}"

	async with AsyncClient() as client:
		response = await client.get(url_request)
		response.raise_for_status()

	data = response.json()

	currency_list: list = [currency, new_currency]
	response_dict: dict = {}

	for cur in currency_list:
		if cur in data['data']:
			response_dict[cur] = data['data'][cur]['value']

	return response_dict


asyncio.run(get_data_to_api_coin_market(currency="RUB", new_currency="EUR"))
