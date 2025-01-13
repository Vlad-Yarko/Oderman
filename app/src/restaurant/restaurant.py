from flask import render_template, Blueprint, request
from app.src.databases.requests import orm_pizza_menu, orm_beverages_menu

restaurant = Blueprint('restaurant', __name__, template_folder='templates', static_folder='static')


@restaurant.route('/menu/pizza')
async def pizza_menu():
    piz_menu = await orm_pizza_menu()
    is_sort = request.args.get('sort')
    if is_sort:
        piz_menu = sorted(piz_menu, key=lambda x: x.price)
    return render_template('restaurant_t/universal_menu.html', menu=piz_menu,
                           title='Pizza',
                           food_title='Pizza',
                           bg='warning')


@restaurant.route('/menu/beverages')
async def beverages_menu():
    bev_menu = await orm_beverages_menu()
    is_sort = request.args.get('sort')
    if is_sort:
        bev_menu = sorted(bev_menu, key=lambda x: x.price)
    return render_template('restaurant_t/universal_menu.html', menu=bev_menu,
                           title='Beverages',
                           food_title='Beverages',
                           bg='info')


@restaurant.route('/menu')
async def all_menu():
    bev_menu = await orm_beverages_menu()
    piz_menu = await orm_pizza_menu()
    is_sort = request.args.get('sort')
    if is_sort:
        piz_menu = sorted(piz_menu, key=lambda x: x.price)
        bev_menu = sorted(bev_menu, key=lambda x: x.price)
    return render_template('restaurant_t/all_menu.html', menu_bev=bev_menu,
                           title='Menu',
                           menu_piz=piz_menu)
