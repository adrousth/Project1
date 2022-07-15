from exception.exceptions import *
from service.request_service import RequestService
from flask import request, Blueprint


request_ctrl = Blueprint('request_controller', __name__)
request_service = RequestService()


@request_ctrl.route("/", methods=["GET"])
def get_all_requests():
    return {
        "requests": request_service.get_all_requests()
    }


