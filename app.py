from flask import Flask
from controller.user_controller import user_ctrl
from controller.request_controller import request_ctrl


print(__name__)
if __name__ == '__main__':

    app = Flask(__name__)
    app.register_blueprint(user_ctrl)
    app.register_blueprint(request_ctrl)
    app.run(port=8080, debug=True)

