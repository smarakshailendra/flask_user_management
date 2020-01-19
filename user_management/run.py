from flask import Flask, request, jsonify
from app.services.login import user_login
from app.services.logout import user_logout
from app.services.get_users import get_user_list
app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    role = request.json.get("role")
    resp = user_login(username=username, password=password, role=role)
    return resp


@app.route('/logout', methods=["POST"])
def logout():
    username = request.json.get("username")
    resp = user_logout(username=username)
    return resp


@app.route('/get_users', methods=["POST"])
def get_users():
    username = request.json.get("username")
    res = get_user_list(username=username)
    if isinstance(res, list):
        return jsonify(res)
    else:
        return res


if __name__ == '__main__':
    app.run()