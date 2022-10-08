from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   flash)
from flask_login import login_user, logout_user
from webapp.auth.models import db, User
from .forms import LoginForm, RegisterForm

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("user:", form.username.data)
    print("psw:", form.password.data)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember.data)
        flash("Você está dentro do sistema.", category="success")
        return redirect(url_for('sistema.index'))

    return render_template('login.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Você saiu do sistema.", category="success")
    return redirect(url_for('main.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Usuário foi criado com sucesso.", category="success")
        return redirect(url_for('.login'))

    return render_template('register.html', form=form)
