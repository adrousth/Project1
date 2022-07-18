from flask import Flask
from controller.user_controller import user_ctrl
from controller.request_controller import request_ctrl
from flask_cors import CORS


if __name__ == '__main__':

    app = Flask(__name__)
    app.secret_key = 'cannot elope'
    app.config['SESSION_TYPE'] = 'filesystem'
    CORS(app, supports_credentials=True, origins="http://127.0.0.1:5500")
    app.register_blueprint(user_ctrl)
    app.register_blueprint(request_ctrl)
    app.run(port=8080, debug=True)
