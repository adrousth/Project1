from exception.exceptions import *
from service.user_service import UserService
from flask import request, Blueprint, session

user_ctrl = Blueprint('user_controller', __name__)
user_service = UserService()


@user_ctrl.route('/')
def user_status():
    user_info = session.get("user_info")
    if user_info is None:
        return False
    else:
        return True


@user_ctrl.route("/get-user", methods=["GET"])
def get_user():
    return user_service.get_user_by_username('').to_dict()


@user_ctrl.route("/login", methods=["POST"])
def login_user():

    data = request.get_json()

    try:
        user = user_service.login_user(data)
        session['user_info'] = user
        print("logged in user", session.get('user_info'))
        return {
            "user_info": user
               }, 200
    except LoginError as e:
        print(e)
        return {
            "message": str(e)
        }, 400


@user_ctrl.route('/login-status', methods=['GET'])
def login_status():
    print("login user", session.get('user_info'))

    if session.get('user_info') is not None:
        return {
            "login_status": True,
            "message": "You are logged in",
            "logged_in_user": session.get('user_info')
        }, 200
    else:
        return {
            "login_status": False,
            "message": "You are not logged in"
        }, 200


@user_ctrl.route('/logout', methods=['POST'])
def logout():
    session.clear()

    return {
        "message": "Successfully logged out"
    }, 200



