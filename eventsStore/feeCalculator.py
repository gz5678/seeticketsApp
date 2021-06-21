from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from eventsStore import db
from eventsStore.models import Events, Products, association_table

bp = Blueprint('calculators', __name__)


@bp.route('/')
def chooseEvent():
    events = Events.query.with_entities(Events.name).all()
    eventNames = [event.name for event in events]
    return render_template('chooseEvent.html', events=eventNames)


@bp.route('/chooseProducts')
def chooseProducts():
    error = None
    eventName = request.args.get('event')
    event = Events.query.filter_by(name=eventName).first()
    if not event:
        error = "No event was given or event doesn't exist"
        flash(error)
        return redirect(url_for('calculators.chooseEvent'))
    else:
        products = Products.query.join(association_table,
                                       association_table.c.product_id == Products.id).\
            filter(association_table.c.event_id == event.id)
        productsNames = [product.name for product in products]
        return render_template('chooseProducts.html', products=productsNames)
