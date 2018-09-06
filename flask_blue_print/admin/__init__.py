# -*- coding: utf-8 -*-
from flask import Blueprint

admin_blue = Blueprint("admin", __name__, url_prefix="/admin", static_folder="static")


@admin_blue.route('/')
def admin():
    return "admin"
# from admin import admin_route
