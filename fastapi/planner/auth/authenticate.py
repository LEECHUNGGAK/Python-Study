from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from auth.jwt_handler import verity_access_token


oath2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="/user/signin")

async def authenticate(token: str = Depends(oath2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=".",
        )
    
    decoded_token = verity_access_token(token)
    return decoded_token["user"]