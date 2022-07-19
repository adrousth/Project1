from flask import Flask
from controller.user_controller import user_ctrl
from controller.request_controller import request_ctrl
from flask_cors import CORS
from flask_session import Session


if __name__ == '__main__':

    app = Flask(__name__)
    app.secret_key = 'cannot elope'
    app.config['SESSION_TYPE'] = 'filesystem'
    CORS(app, supports_credentials=True)
    Session(app)
    app.register_blueprint(user_ctrl)
    app.register_blueprint(request_ctrl)
    app.run(port=8080, debug=True)
