from dao.user_dao import UserDao


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def get_user_by_username(self, username):
        user = self.user_dao.get_user_by_username(username)





