from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
import sqlite3 as sql
import os.path
from app.model import Log

main = Blueprint('main', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '/../../', "app.db")

@main.route('/')
@main.route('/index')
@login_required
def index():
    #
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from main.calc")
    calcs = cur.fetchall()
    con.close()
    return render_template('main/index.html', calcs=calcs)


@main.route('/log')
@login_required
def log():
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from main.calc_log")
    logs = cur.fetchall()
    con.close()
    return render_template('main/log.html', logs=logs)


@main.route('/admin')
@login_required
def admin():
    comments = [{'id': 1, 'name': 'dani', 'city': 'kras'}, {'id': 2, 'name': 'sanc', 'city': 'rostov'}]
    return render_template('main/admin.html')


@main.route("/delete", methods=["POST"])
@login_required
def delete():
    print("delete")
    return render_template('main/admin.html')
