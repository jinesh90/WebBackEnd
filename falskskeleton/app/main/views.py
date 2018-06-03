from flask import render_template, session, redirect, url_for
from . import main




@main.route('/')
def index():
    return "Hello Jinesh"


