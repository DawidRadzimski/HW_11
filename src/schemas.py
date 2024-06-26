from datetime import date
from pydantic import BaseModel, Field, validator
from typing import Optional


class ContactIn(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=100)
    phone_number: str = Field(max_length=15)
    date_of_birth: date = None
    additional_data: str = Field(max_length=500)

    @validator('date_of_birth', pre=True)
    def check_date_format(cls, birthday_date):
        if isinstance(birthday_date, str):
            if birthday_date == "":
                return None
            try:
                return date.fromisoformat(birthday_date)
            except ValueError:
                raise ValueError(
                    "Invalid date format. Required format: YYYY-MM-DD")
        return birthday_date


class ContactOut(ContactIn):
    id: int

    class Config:
        orm_mode = True


class ContactUpdate(BaseModel):
    first_name: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    date_of_birth: Optional[date] = None
    additional_data: Optional[str]

    @validator("date_of_birth", pre=True)
    def check_date_format(cls, birthday_date):
        if isinstance(birthday_date, str):
            if birthday_date == "":
                return None
            try:
                return date.fromisoformat(birthday_date)
            except ValueError:
                raise ValueError(
                    "Invalid date format. Required format: YYYY-MM-DD")
        return birthday_date


class ContactDelete(ContactIn):
    id: int

    class Config:
        orm_mode = True