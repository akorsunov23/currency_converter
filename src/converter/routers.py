from fastapi import APIRouter, Depends
from src.converter.schemas import DataConverted
converter_app = APIRouter(
	tags=["Converter"],
	prefix="/converter"
)


@converter_app.get('')
async def currency_converted(
		data: DataConverted = Depends(DataConverted)
):
	"""Конвертация валют по заданным параметрам."""
	print(data)
	return {'msg': 'Cool'}
