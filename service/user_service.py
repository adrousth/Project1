from model.user import User
from dao.user_dao import UserDao


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def get_user_by_username(self, username):
        user = self.user_dao.get_user_by_username(username)
        return User(user[0], user[1], user[2], user[3], user[4], user[5])





