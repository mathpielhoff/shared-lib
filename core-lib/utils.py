from jose import JWTError, jwt
from model.LoginResponse import LoginResponse
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, status



def decode_jwt(token: str) -> LoginResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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