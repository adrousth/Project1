from exception.exceptions import *
from service.request_service import RequestService
from flask import request, Blueprint


request_ctrl = Blueprint('request_controller', __name__)
request_service = RequestService()


@request_ctrl.route("/", methods=["GET"])
def get_all_requests():
    return {
        "requests": request_service.get_all_requests()
    }, 200


@request_ctrl.route("/requests", methods=["POST"])
def add_new_request():
    data = request.get_json()
    # TODO add logged in user
    user_id = 1
    try:
        returned_request = request_service.add_new_request(data, user_id)
        return {
                   "request": returned_request
               }, 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


