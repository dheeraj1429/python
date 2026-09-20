from pydantic import BaseModel, Field, field_validator, model_validator, computed_field, ConfigDict
from typing import List, Dict, Optional, Union
from datetime import date, datetime

class Address(BaseModel):
  street: str
  city: str
  postal_code: str

class User(BaseModel):
  name: str
  created_at: datetime
  address: Address

  model_config = ConfigDict(
    json_encoders={
      datetime: lambda x: x.strftime("%d-%m-%y %H:%M:%S")
    }
  )

user_data = {
  "name": "Demo",
  "created_at": date.today(),
  "address": {
    "street": "01-street",
    "city": "Demo city",
    "postal_code": "123abc"
  }
}

u = User(**user_data)
print(u.model_dump())
print("="*30)
print(u)
print("="*30)
print(u.model_dump_json())

# class Address(BaseModel):
#   street: str
#   city: str
#   postal_code: str

# class Company(BaseModel):
#   name: str
#   address: Optional[Address] = None

# class Employee(BaseModel):
#   name: str
#   company: Optional[Company] = None

# class TextContent(BaseModel):
#   title: str
#   content: str

# class ImageContent(BaseModel):
#   type: str
#   url: str
#   alt_text: str

# class Article(BaseModel):
#   title: str
#   section: List[Union[TextContent, ImageContent]]

# class Comment(BaseModel):
#   id: int
#   content: str
#   replies: Optional[List["Comment"]] = None

# Comment.model_rebuild()

# c2 = Comment(
#   id=2,
#   content="Hi there!"
# )

# c1 = Comment(
#   id=1,
#   content="Hello there",
#   replies=[c2]
# )

# print(c1)

# class Address(BaseModel):
#   street: str
#   city: str
#   postal_code: str

# class User(BaseModel):
#   id: int
#   name: str
#   address: Address

# address = Address(
#   street="0123",
#   city="DemoCity",
#   postal_code="123ABC"
# )
# user = User(
#   id=1,
#   name="DemoUser",
#   address=address
# )
# print(user)

# class Product(BaseModel):
#   price: float
#   start_date: datetime
#   end_date: datetime

#   @field_validator("price", mode='before')
#   def parse_price(cls, v):
#     if isinstance(v, str):
#       return float(v.replace("$", "").replace(",", ""))

#   @model_validator(mode="after")
#   def validate_date_range(cls, values):
#     if values.start_date >= values.end_date:
#       raise ValueError("Start date will be less then end date")
#     return values

# p = Product(
#   price="$123.2",
#   start_date=date.today(),
#   end_date=date.today()
# )
# print(p)

# class User(BaseModel):
#   email: str

#   @field_validator("email")
#   def normalize_email(cls,v):
#     return v.lower().strip()

# class Person(BaseModel):
#   first_name: str
#   last_one: str

#   @field_validator("first_name", "last_name")
#   def name_must_be_capitalize(cls, v):
#     if not v.istitle():
#       raise ValueError("Name must be capitalize")
#     return v

# p = Person(
#   first_name="Demo",
#   last_one="Name"
# )

# class Booking(BaseModel):
#   user_id: int
#   room_id: int
#   nights: int = Field(
#     ...,
#     ge=1
#   )
#   rate_per_night: float

#   @computed_field
#   @property
#   def total_amount(self) -> float:
#     return self.nights * self.rate_per_night

# b1 = Booking(
#   user_id=1,
#   room_id=1,
#   nights=2,
#   rate_per_night=10
# )

# b2 = Booking(
#   user_id=2,
#   room_id=2,
#   nights=2,
#   rate_per_night=20
# )

# print(b1, b2)

# class Product(BaseModel):
#   price: float = Field(
#     ...,
#     ge=0,
#     le=100
#   )
#   quantity: int = Field(
#     ...,
#     ge=0,
#     le=10
#   )

#   @computed_field
#   @property
#   def total_price(self) -> float:
#     return self.price * self.quantity

# p1 = Product(
#   price=100,
#   quantity=2
# )

# print(p1.total_price)

# class User(BaseModel):
#   username: str

#   @field_validator('username')
#   def username_length(cls, v):
#     if len(v) > 4:
#       raise ValueError("Username must be less then 4 characters")
#     return v

# class Signup(BaseModel):
#   password: str = Field(
#     ...,
#     min_length=4,
#     max_length=10
#   )
#   confirm_password = str

#   @model_validator(mode="after")
#   def password_match(cls, values):
#     if values.password != values.confirm_password:
#       raise ValueError("Password do not match")
#     return values

# class Employee(BaseModel):
#   id: int
#   name: str = Field(
#     ...,
#     min_length=3,
#     max_length=50,
#     description="Employee example",
#     examples="Demo name"
#   )
#   department: Optional[str]
#   salary: float = Field(
#     ...,
#     ge=10000,
#     le=100000,
#   )

# class Cart(BaseModel):
#   user_id: int
#   items: List[str]
#   quantities: Dict[str, int]

# class Blog(BaseModel):
#   title: str
#   content: str
#   image_url: Optional[str] = None

# class Product(BaseModel):
#   id: int
#   name: str
#   price: float
#   in_stock: bool = True

# product_one = Product(id=1, name="Laptop", price=99.9, in_stock=True)
# product_two = Product(id=1, name="Laptop", price=99.9)
# product_three = Product(name="Keyboard")


# class User(BaseModel):
#   id: int
#   name: str
#   is_active: bool

# user_data = {"id": 123, "name": "demo_user", "is_active": True}

# user = User(**user_data)
# print(user)