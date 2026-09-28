from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr
from jwt_service import create_access_token
from password_service import create_hash_password, verify_password

router = APIRouter()

class CreateAccount(BaseModel):
  email: EmailStr
  password: str

class CreateAccountResponse(BaseModel):
  access_token: str

user: CreateAccount | None = None

class Login(CreateAccount):
  pass

@router.post('/login', status_code=status.HTTP_200_OK, response_model=CreateAccountResponse)
async def login(payload: Login):
  if payload.email != user.email:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please provide the correct email address!")
  if not verify_password(password=payload.password, hash=user.password):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please provide the correct password!")
  access_token = create_access_token(payload.model_dump(exclude={"password"}))
  return CreateAccountResponse(access_token=access_token)

@router.post("/create-account", status_code=status.HTTP_201_CREATED, response_model=CreateAccountResponse)
async def create_account(payload: CreateAccount):
  global user
  user = payload
  access_token = create_access_token(payload.model_dump(exclude={"password"}))
  hash_password = create_hash_password(password=payload.password)
  user.password = hash_password
  return CreateAccountResponse(access_token=access_token)