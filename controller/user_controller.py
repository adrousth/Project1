from exception.exceptions import *
from service.user_service import UserService
from flask import request, Blueprint


user_ctrl = Blueprint('user_controller', __name__)
user_service = UserService()


@user_ctrl.route("/get-user", methods=["GET"])
def get_user():
    return user_service.get_user_by_username('adrousth').to_dict()

