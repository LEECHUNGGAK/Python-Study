import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError

from database.connection import Settings

settings = Settings()

def create_access_token(user: str):
    token = jwt.encode(
        algorithm="HS256",
        payload={
            "user": user,
            "expires": time.time() + 3600
        },
        key=settings.SECREAT_KEY,
    )
    return token

def verity_access_token(token: str):
    try:
        data = jwt.decode(
            token=token,
            key=settings.SECREAT_KEY,
            algorithms="HS256",
        )

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token.",
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!",
            )
            
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token.",
        )
    
    else:
        return data
