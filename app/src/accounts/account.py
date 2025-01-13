from flask import request, redirect, render_template, flash, url_for, session, Blueprint
from app.src.databases.requests import orm_find_account, orm_create_account, orm_update_profile_image
from werkzeug.security import check_password_hash, generate_password_hash
from app.src.accounts.forms.forms import SignUp, LogIn
from secrets import token_hex

account = Blueprint('accounts', __name__, template_folder='templates', static_folder='static')


@account.route('/signup', methods=['POST', 'GET'])
async def sign_up_site():
    signup_form = SignUp()
    mode = request.args.get('mode')
    if signup_form.validate_on_submit():
        user_name = signup_form.username.data
        user_password = signup_form.password.data
        user_password_hash = generate_password_hash(user_password)
        u = await orm_find_account(user_name)
        if not u:
            flash('You signed up successfully', category='success')
            await orm_create_account(user_name, user_password_hash)
            if mode:
                return redirect(url_for('home', mode=mode))
            return redirect(url_for('home'))
        else:
            flash('Username is already busy', category='error')
            if mode:
                return redirect(url_for('accounts.sign_up_site', mode=mode))
            return redirect(url_for('accounts.sign_up_site'))
    else:
        return render_template('account_t/signup.html', form=signup_form)


@account.route('/login', methods=['GET', 'POST'])
async def login_site():
    loin_form = LogIn()
    mode = request.args.get('mode')
    if loin_form.validate_on_submit():
        user_name = loin_form.username.data
        user_password = loin_form.password.data
        is_remember = loin_form.remember_me.data
        u = await orm_find_account(user_name)
        if u:
            if check_password_hash(u.password, user_password):
                flash('You logged in successfully', category='success')
                session['usr'] = user_name
                if mode:
                    return redirect(url_for('home', mode=mode))
                return redirect(url_for('home'))
            else:
                flash('Incorrect password or username', category='error')
                if mode:
                    return redirect(url_for('accounts.login_site', mode=mode))
                return redirect(url_for('accounts.login_site'))
        else:
            flash('Incorrect password or username', category='error')
            if mode:
                return redirect(url_for('accounts.login_site', mode=mode))
            return redirect(url_for('accounts.login_site'))
    else:
        usr = session.get('usr', "")
        if usr:
            flash('You have already logging in', category='error')
            if mode:
                return redirect(url_for('home', mode=mode))
            return redirect(url_for('home'))
        else:
            return render_template('account_t/login.html', form=loin_form)


@account.route('/logout')
async def logout_site():
    user = session.get('usr', "")
    mode = request.args.get('mode')
    if user:
        session['usr'] = ""
        flash('You logged out successfully', category='success')
        if mode:
            return redirect(url_for('home', mode=mode))
        return redirect(url_for('home'))
    else:
        flash('You are not logged in', category='error')
        if mode:
            return redirect(url_for('home', mode=mode))
        return redirect(url_for('home'))


@account.route('/profile')
async def user_profile():
    username = session.get('usr', "")
    mode = request.args.get('mode')
    if username:
        user = await orm_find_account(user_name=username)
        img_path = user.image_path
        return render_template("account_t/profile.html", username=username, image=img_path)
    else:
        flash('You are not logged in', category='error')
        if mode:
            return redirect(url_for('home', mode=mode))
        return redirect(url_for('home'))


@account.route('/profile/update_image', methods=['POST', 'GET'])
async def update_image():
    username = session.get('usr', '')
    mode = request.args.get('mode')
    if request.method == 'POST':
        if username:
            file = request.files['file']
            file_name = file.filename
            file_extension = file_name.split('.')[-1]
            if file_extension.lower() in ('png', 'jpg', 'jpeg'):
                hex = token_hex(8)
                file_n = hex + '.' + file_extension
                file.save(f'C:/Projects/Oderman/Oderman/app/src/accounts/static/images/{file_n}')
                await orm_update_profile_image(username, image_path=file_n)
                flash("Profile image was updated successfully", category='success')
                if mode:
                    return redirect(url_for('accounts.user_profile', mode=mode))
                return redirect(url_for('accounts.user_profile'))
            else:
                flash('Incorrect type of image', category="error")
                if mode:
                    return redirect(url_for('accounts.update_image', mode=mode))
                return redirect(url_for('accounts.update_image'))
        else:
            flash('You are not logged in', category='error')
            if mode:
                return redirect(url_for('home', mode=mode))
            return redirect(url_for('home'))
    else:
        if username:
            return render_template("account_t/up_image.html")
        else:
            flash('You are not logged in', category='error')
            if mode:
                return redirect(url_for('home', mode=mode))
            return redirect(url_for('home'))
