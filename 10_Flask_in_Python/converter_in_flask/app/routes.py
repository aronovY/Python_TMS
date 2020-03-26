import flask
from app import app, uri, db
from flask import render_template, redirect
from app.forms import LoginForm, RegisterForm, CurrencyForm
from app.calculate import calculation
from app.req import get_data_from_uri
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, History, Money
from werkzeug.urls import url_parse


get_data_from_uri(uri)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(flask.url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user is None or not user.check_password(form.password.data):
            flask.flash('Invalid username or password')
            return redirect(flask.url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = flask.request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = flask.url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(flask.url_for('login'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(flask.url_for('login'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, surname=form.surname.data,
                    login=form.login.data, email=form.email.data,
                    password=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flask.flash('Congratulations, you are now a registered user!')
        return redirect(flask.url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', title='Home')


@app.route('/convert', methods=['GET', 'POST'])
@login_required
def convert():
    user = User.query.filter_by(login=current_user.login).first()
    all_money = Money.query.filter_by().all()
    form = CurrencyForm()
    if form.validate_on_submit():
        res = calculation(form.first_cur.data, form.how_much.data, form.second_cur.data, user.id)
        return render_template('result.html',
                               user=user,
                               first=form.first_cur.data,
                               how_m=form.how_much.data,
                               second=form.second_cur.data,
                               res=res)
    return render_template('convert.html', title='Convert', form=form, all_money=all_money)


@app.route('/result', methods=['GET'])
@login_required
def result(first, how_m, second, res):
    return render_template('result.html',
                           user=user,
                           first=first,
                           how_m=how_m,
                           second=second,
                           res=res)


@app.route('/user/<login>')
@login_required
def user(login):
    user = User.query.filter_by(login=login).first_or_404()
    history = History.query.filter_by(user_id=user.id).all()
    return render_template('user.html', user=user, history=history)

