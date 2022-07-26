from exception.exceptions import *
from service.request_service import RequestService
from flask import request, Blueprint, session, render_template


request_ctrl = Blueprint('request_controller', __name__)
request_service = RequestService()


@request_ctrl.route("/requests", methods=["GET"])
def get_all_requests_for_user():
    user_info = session.get("user_info")
    if user_info is None:
        return {
            "message": "you cannot view requests when you are not logged in."
        }, 400

    return {
        "requests": request_service.get_all_requests_for_user(user_info["user_id"])
    }, 200


@request_ctrl.route("/manager/requests", methods=["GET"])
def get_all_requests_manager():
    user_info = session.get("user_info")
    print(user_info)
    if user_info is None:
        return {
            "message": "you cannot view requests when you are not logged in."
        }, 400
    if user_info["user_role"] != "finance_manager":
        return {
            "message": "you cannot view all requests if you are not a finance manager"
        }, 400
    return {
        "requests": request_service.get_all_requests()
    }, 200


@request_ctrl.route("/requests", methods=["POST"])
def add_new_request():
    data = request.form
    receipt = type(request.files['receipt'])
    user_info = session.get("user_info")
    print(data)
    print(receipt)

    if user_info is None:
        return {
            "message": "you cannot create a request when you are not logged in."
        }, 400
    try:

        returned_request = request_service.add_new_request(data, receipt, user_info['user_id'])
        return {
                   "request": returned_request
               }, 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


@request_ctrl.route("/request/<request_id>")
def get_request_by_id(request_id):
    try:
        returned_request = request_service.get_request_by_id(request_id)
        return render_template("request.html", request=returned_request)
    except RequestNotFoundError as e:
        return {
            "message": e
        }, 404


@request_ctrl.route("/update-requests", methods=["POST"])
def update_requests():
    data = request.get_json()
    user_info = session.get("user_info")
    print(data)
    if user_info is None:
        return {
                   "message": "you cannot update a request when you are not logged in."
               }, 400
    try:
        user_id = user_info["user_id"]
        returned_request = request_service.update_requests(data, user_id)
        print(returned_request)
        return {
                   "requests": returned_request
               }, 201
    except InvalidParameterError as e:
        return {
                   "message": str(e)
               }, 400
