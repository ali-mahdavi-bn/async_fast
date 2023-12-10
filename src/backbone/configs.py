# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = True
    EXPIRE_OTP_CODE: int = 120
    POSTGRES_USER: str = "lib"
    POSTGRES_PASSWORD: str = "lib"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DATABASE: str = "lib"
    REDIS_HOST: str = "redis"
    REDIS_PORT: str = "6379"
    TOKEN_VALID: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDE2MDM3MzUsInN1YiI6IjE1In0.xtZBBr3SCappzMObvr6afNCE5g3Li_rRCtPy2a25JDI"

    # class Config:
    #     case_sensitive = False
    #     BASE_DIR = Path(__file__).resolve().parent.parent.parent
    #     env_file = (str(BASE_DIR) + "/.env").replace("//", "/")
    #     env_file_encoding = 'utf-8'


config = Config()


class PasswordConfig:
    MIN_LENGTH = 8
    UPPERCASE_REQUIRED = False
    LOWERCASE_REQUIRED = True
    DIGIT_REQUIRED = True
    SPECIAL_CHARACTERS_REQUIRED = False
    SPECIAL_CHARACTERS = r"[!@#$%^&*()]"
