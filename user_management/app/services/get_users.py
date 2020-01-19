from app.utils.utils import check_authenticated, rbac
from app.utils.db_connection import create_session

from app.db import models
from flask import Response

@rbac
@check_authenticated
def get_user_list(*args,**kwargs):
    auth_status = kwargs.get("auth_status")
    is_authorized = kwargs.get("is_authorized")
    if not auth_status:
        return Response("User logged out. Please login again.")
    if not is_authorized:
        return Response("Unauthorized access.")
    auth_tab = models.auth_table
    sess = create_session()
    res = sess.query(auth_tab.columns.id, auth_tab.columns.username).all()
    return res
