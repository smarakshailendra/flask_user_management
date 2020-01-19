from flask import Response

from app.db import models
from app.utils.db_connection import create_session


def user_login(username, password, role="user"):
    if not username or not password:
        return Response("Please provide username and password")

    auth_tab = models.auth_table
    # register_user(auth_tab, username, password, role)
    sess = create_session()
    res = sess.query(auth_tab.columns.username, auth_tab.columns.password).filter(
        auth_tab.columns.username == username).all()
    if not res:
        return Response("Incorrect Username provided", 404)
    elif len(res) > 1:
        return Response("Duplicate user found. Unable to login.", 500)
    else:
        if res[0][1] != password:
            return Response("Incorrect password. Please enter correct password.", 401)
        else:
            stmt = auth_tab.update().where(auth_tab.columns.username == username).values({"auth_status": True})
            sess.execute(stmt)
            sess.commit()
            return Response("Authenticated.", 200)
