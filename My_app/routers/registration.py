from My_app import app
from flask import request, redirect, render_template, flash, url_for, session
from My_app.databases.requests import orm_find_account, orm_create_account


@app.route('/signup', methods=['POST', 'GET'])
async def sign_up_site():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['password']
        u = await orm_find_account(user_name)
        if not u:
            flash('You signed up successfully', category='success')
            await orm_create_account(user_name, user_password)
            return redirect(url_for('home'))
        else:
            flash('Username is already busy', category='error')
            return redirect(url_for('sign_up_site'))
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
async def login_site():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['password']
        u = await orm_find_account(user_name)
        if u:
            if user_password == u.password:
                session.permanent = True
                flash('You logged in successfully', category='success')
                session['usr'] = request.form['user_name']
                return redirect(url_for('home'))
            else:
                flash('Incorrect password or username', category='error')
                return redirect(url_for('login_site'))
        else:
            flash('Incorrect password or username', category='error')
            return redirect(url_for('login_site'))
    else:
        usr = session.get('usr', "")
        if usr:
            flash('You have already logging in', category='error')
            return redirect(url_for('home'))
        else:
            return render_template('login.html')


@app.route('/logout')
async def logout_site():
    usr = session.get('usr', "")
    if usr:
        session['usr'] = ""
        flash('You logged out successfully', category='success')
        return redirect(url_for('home'))
    else:
        flash('You are not logged in', category='error')
        return redirect(url_for('home'))
