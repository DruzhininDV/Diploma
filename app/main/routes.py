from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    comments = [{'id': 1, 'name': 'Расчет для систем хранения', 'prior': 3},
                {'id': 2, 'name': 'Цены продажи', 'prior': '2'},
                {'id': 3, 'name': 'Расчет входных цен', 'prior': '5'}
                ]
    return render_template('main/index.html', comments=comments)


@main.route('/log')
@login_required
def log():
    comments = [{'id': 1, 'name': 'dani', 'city': 'kras'}, {'id': 2, 'name': 'sanc', 'city': 'rostov'}]
    return render_template('main/log.html')


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
