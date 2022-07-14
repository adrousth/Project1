from exception.exceptions import *

from flask import request, Blueprint


user_ctrl = Blueprint('user_controller', __name__)


@user_ctrl.route("/", methods=["GET"])
def get_user():
    pass

