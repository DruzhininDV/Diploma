from flask import Blueprint, render_template, redirect, url_for, request
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
    cur.execute("select * from main.calc_log order by id desc ")
    logs = cur.fetchall()
    con.close()
    return render_template('main/log.html', logs=logs)


@main.route('/admin')
@login_required
def admin():
    comments = [{'id': 1, 'name': 'dani', 'city': 'kras'}, {'id': 2, 'name': 'sanc', 'city': 'rostov'}]
    return render_template('main/admin.html')


@main.route('/add_log', methods=["POST"])
@login_required
def add_log():
    name = request.form["name"]
    id_calc = request.form["id_calc"]
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("INSERT INTO main.calc_log (time,id_calc,status,name,startdate,enddate,calcdate) "
                "VALUES(null, ?, 0, ?, datetime('now'), null , datetime('now'))", (id_calc, name))
    con.commit()
    con.close()
    return redirect(url_for('main.log'))


#
@main.route('/delete_log', methods=["POST"])
@login_required
def delete_log():
    id = request.form["id"]
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute(
        "UPDATE main.calc_log SET time = (select strftime('%M','now', 'localtime') - strftime('%M', startdate) "
        "from main.calc_log where  id =?), status = 2, enddate = datetime('now') where id = ?;", (id, id))
    con.commit()
    con.close()
    return redirect(url_for('main.log'))

# @main.route("/delete", methods=["POST"])
# @login_required
# @app.route("/comment_delete", methods=["POST"])
# def comment_delete():
#     id = request.form["id"]
#     db_handler.delete_comment_by_id(id)
#     return redirect(url_for('view'))
