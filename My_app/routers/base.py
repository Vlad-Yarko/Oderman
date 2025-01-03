from My_app import app
from flask import render_template, session
from My_app.databases.requests import orm_pizza_menu, orm_beverages_menu


@app.route('/')
async def home():
    usr = session.get('usr', "")
    return render_template('index.html', user=usr)


@app.route('/menu/pizza')
async def pizza_menu():
    piz_menu = await orm_pizza_menu()
    return render_template('universal_menu.html', menu=piz_menu, title='Pizza', food_title='Pizza', bg='warning')


@app.route('/menu/beverages')
async def beverages_menu():
    bev_menu = await orm_beverages_menu()
    return render_template('universal_menu.html', menu=bev_menu, title='Beverages', food_title='Beverages', bg='info')


@app.route('/menu')
async def all_menu():
    bev_menu = await orm_beverages_menu()
    piz_menu = await orm_pizza_menu()
    return render_template('all_menu.html', menu_bev=bev_menu, title='Menu', menu_piz=piz_menu)
