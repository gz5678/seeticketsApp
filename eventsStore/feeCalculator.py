from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from eventsStore import db
from eventsStore.models import Events, Products, association_table

bp = Blueprint('calculators', __name__)


@bp.route('/')
def chooseEvent():
    events = Events.query.all()
    eventNames = [event.name for event in events]
    return render_template('chooseEvent.html', events=eventNames)


@bp.route('/chooseProducts', methods=('GET', 'POST'))
def chooseProducts():
    eventName = request.args.get('event')
    eventId = Events.query.filter_by(name=eventName).first().id
    products = Products.query.join(association_table,
                                   association_table.c.product_id == Products.id).\
        filter(association_table.c.event_id == eventId)
    # products = Products.query.filter(Products.id.in_(productIds)).all()
    productsNames = [product.name for product in products]
    return render_template('chooseProducts.html', products=productsNames)