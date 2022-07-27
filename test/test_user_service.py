import pytest
from service.user_service import UserService
from model.user import User
from exception.exceptions import *

user_service = UserService()


def test_login_user_positive(mocker):
    def mock_get_user_by_username_and_password(self, username, password):
        if username == "btables" and password == "foobar":
            return 1, "btables", "bobby", "tables", "btables@email.net", "finance_manager"
        else:
            return None
    mocker.patch('dao.user_dao.UserDao.get_user_by_username_and_password', mock_get_user_by_username_and_password)
    actual = user_service.login_user({"username": "btables", "password": "foobar"})
    assert User(1, "btables", "bobby", "tables", "btables@email.net", "finance_manager").to_dict() == actual

    with pytest.raises(LoginError) as exception_info:
        user_service.login_user({"username": "btable", "password": "foobar"})
    assert str(exception_info.value) == "Invalid username/password"


def test_login_user_negative(mocker):
    def mock_get_user_by_username_and_password(self, username, password):
        if username == "btables" and password == "foobar":
            return 1, "btables", "bobby", "tables", "btables@email.net", "finance_manager"
        else:
            return None
    mocker.patch('dao.user_dao.UserDao.get_user_by_username_and_password', mock_get_user_by_username_and_password)
    actual = user_service.login_user({"username": "btables", "password": "foobar"})
    assert User(1, "btables", "bobby", "tables", "btables@email.net", "finance_manager").to_dict() == actual

    with pytest.raises(LoginError) as exception_info:
        user_service.login_user({"username": "btable", "password": "foobar"})
    assert str(exception_info.value) == "Invalid username/password"

    with pytest.raises(LoginError) as exception_info:
        user_service.login_user({"username": "btables", "password": "password"})
    assert str(exception_info.value) == "Invalid username/password"








