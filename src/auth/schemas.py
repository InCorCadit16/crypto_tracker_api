from pydantic import BaseModel, Field, SecretStr


class UserRequest(BaseModel):
    username: str = Field(min_length=8, max_length=24)
    password: SecretStr = Field(min_length=8)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
