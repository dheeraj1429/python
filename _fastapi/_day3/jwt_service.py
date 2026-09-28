from fastapi import HTTPException, status
from datetime import datetime, timezone, timedelta
from typing import Optional
import jwt

SECRET_KEY = "YOUR_SUPER_SECRET_KEY_CHANGE_THIS_IN_PRODUCTION"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
  return jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return payload
  except jwt.ExpiredSignatureError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Token has expired",
      headers={"WWW-Authenticate": "Bearer"},
    )
  except jwt.PyJWTError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication token",
      headers={"WWW-Authenticate": "Bearer"}
    )
  except Exception as error:
    raise error