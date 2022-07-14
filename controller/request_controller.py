from exception.exceptions import *

from flask import request, Blueprint


request_ctrl = Blueprint('request_controller', __name__)


@request_ctrl.route("/", methods=["GET"])
def get_requests():
    pass
