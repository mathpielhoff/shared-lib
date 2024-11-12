from jose import JWTError, jwt
from shared_lib.models.LoginResponse import LoginResponse
from shared_lib.utils.config import Config
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from typing import Optional


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

def decode_jwt(token: str) -> LoginResponse:
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        tenant_id: int = payload.get("tenantId")
        print(payload)
        if username is None or role is None or tenant_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token payload invalid",
            )
        return LoginResponse(username=username, tenant_id=tenant_id, role=role)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired",
        )