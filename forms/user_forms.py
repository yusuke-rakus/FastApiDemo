from pydantic import BaseModel


class UserForm(BaseModel):
    email: str


class LoginForm(BaseModel):
    email: str


class CreateUserForm(BaseModel):
    email: str


class DeleteUserForm(BaseModel):
    user_id: int
    email: str
