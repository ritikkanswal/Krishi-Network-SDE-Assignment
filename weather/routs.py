from flask import Blueprint
from .controller import get

site=Blueprint('site',__name__)

site.route("/get") (get)

