from pydantic import BaseModel, ValidationError , EmailStr, field_validator
from typing import List

#  Basic Pydantic Model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

user_data = {
    "id": 1,
    "name": "Umm e Habiba",
    "email": "ummeyhabiba1312@gmail.com",
    "age": 20
}

user = User(**user_data)
print(user)
print(user.model_dump())


try:
    invalid_user = User(id="not_an_int", name="Umm e Habiba", email="ummeyhabiba1312@gmail.com")
except ValidationError as e:
    print(e)




# Nested Models
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: list[Address]

user_data = {
    "id": 1,
    "name": "Umm e Habiba",
    "email": "ummeyhabiba1312@gmail.com",
    "address": [
        {
        "street": "123 Main St",
        "city": "Karachi",
        "zip_code": "12345"
    },
    {
        "street": "456 Elm St",
        "city": "Lahore",
        "zip_code": "67890"
    }
    ]
    }

user = UserWithAddress.model_validate(user_data)
print(user.model_dump())



# Custom Validation

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: list[Address]
    @field_validator('name')
    def name_must_contain_2_char(cls, v):
        if len(v) < 2:
            raise ValueError('Name must be at least 2 characters long')
        return v


try:
    invalid_user = UserWithAddress(
        id=1,
        name="A",
        email="ummeyhabiba1312@gmail.com",
        address=[
            {
                "street": "123 Main St",
                "city": "Karachi",
                "zip_code": "12345"
            },
            {
                "street": "456 Elm St",
                "city": "Lahore",
                "zip_code": "67890"
            }
        ]
    )
except ValidationError as e:
    print(e)