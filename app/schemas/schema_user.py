from pydantic import BaseModel

# 사용자 등록 요청
class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    age: int

# 사용자 정보 응답 처리
class User(BaseModel):
    username: str
    name: str
    age: int