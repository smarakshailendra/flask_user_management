from app.db import models
from app.utils.db_connection import create_session


def check_authenticated(func):
    def inner(*args, **kwargs):
        username = kwargs.get("username")
        auth_tab = models.auth_table
        sess = create_session()
        res = sess.query(auth_tab.columns.username, auth_tab.columns.auth_status).filter(
            auth_tab.columns.username == username).all()
        if not res or len(res) > 1:
            kwargs.update({"auth_status": False})
        else:
            kwargs.update({"auth_status": True}) if res[0][1] == True else kwargs.update({"auth_status": False})
        return func(**kwargs)

    return inner


def rbac(func):
    def inner(*args, **kwargs):
        username = kwargs.get("username")
        auth_tab = models.auth_table
        sess = create_session()
        res = sess.query(auth_tab.columns.username, auth_tab.columns.role).filter(
            auth_tab.columns.username == username).all()
        if not res or len(res) > 1:
            kwargs.update({"is_authorized": False})
        else:
            kwargs.update({"is_authorized": True}) if res[0][1] == "admin" else kwargs.update({"auth_status": False})
        return func(**kwargs)

    return inner
