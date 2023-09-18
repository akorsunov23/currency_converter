from fastapi import APIRouter, Depends, HTTPException
from httpx import HTTPStatusError

from src.converter.schemas import DataConverted, ConvertedResponse
from src.converter.utils import calculate_converted

converter_app = APIRouter(tags=["Converter"], prefix="/converter")


@converter_app.get("", response_model=ConvertedResponse)
async def currency_converted(
    data: DataConverted = Depends(DataConverted),
) -> ConvertedResponse:
    """
    Конвертация валют по заданным параметрам.
    Коды валют должны соответствовать ISO 4217.
    """
    try:
        date_update, volume = await calculate_converted(
            _from=data.from_currency.upper(),
            _to=data.into_currency.upper(),
            volume=data.quantity,
        )
        return ConvertedResponse(date_update=date_update, answer=volume)

    except HTTPStatusError:
        raise HTTPException(
            status_code=422,
            detail="Произошла ошибка при обработке. "
            "Проверьте данные и повторите попытку.",
        )
