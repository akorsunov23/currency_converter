import datetime

from pydantic import BaseModel


class DataConverted(BaseModel):
    """Схема данных запроса о конвертации."""

    from_currency: str
    into_currency: str
    quantity: int


class ConvertedResponse(BaseModel):
    """Схема ответа на запрос конвертации."""

    date_update: datetime.datetime
    answer: float
