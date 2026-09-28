from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt_service import decode_token

router = APIRouter()
security = HTTPBearer()

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
  token = credentials.credentials
  try:
    return decode_token(token=token)
  except Exception as error:
    print(f"Verify token error: {error}")
    raise error

@router.get("/protected")
async def protected_route(token_payload: dict = Depends(verify_jwt_token)):
  print(f"Token payload: {token_payload}")