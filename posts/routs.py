from flask import Blueprint
from .controller import post,nearby

site=Blueprint('site',__name__)


site.route("/post") (post)
site.route("/nearby") (nearby)
site.route("/get") (get)