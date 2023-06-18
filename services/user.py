from fastapi import Depends

from repositories.user import UserRespository


class UserService:
    def __init__(self, repo: UserRespository = Depends()) -> None:
        self.repo = repo

    async def get_user_by_email(self, email: str):
        return self.repo.get_user_by_email(email)
