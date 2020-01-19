from flask import Response
from app.db import models
from app.utils.db_connection import create_session


def user_logout(username):
    auth_tab = models.auth_table
    # register_user(auth_tab, username, password, role)
    sess = create_session()
    res = sess.query(auth_tab.columns.username, auth_tab.columns.auth_status).filter(auth_tab.columns.username == username).all()
    if not res:
        return Response("Incorrect Username provided", 404)
    elif len(res) > 1:
        return Response("Duplicate user found. Unable to logout.", 500)
    else:
        if res[0][1] == False:
            return Response("Already Logged out.", 500)
        stmt = auth_tab.update().where(auth_tab.columns.username == username).values({"auth_status": False})
        sess.execute(stmt)
        sess.commit()
        return Response("Logged Out user {}.".format(username), 200)