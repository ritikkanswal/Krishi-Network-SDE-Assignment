from flask import Blueprint
from .controller import post,nearby,get,home

site=Blueprint('site',__name__)

site.route("/") (home)
site.route("/post") (post)
site.route("/nearby") (nearby)
site.route("/get") (get)