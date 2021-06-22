import functools

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from eventsStore import db
from eventsStore.models import Events, Products, association_table
from sqlalchemy import func

bp = Blueprint('calculators', __name__)


@bp.route('/')
def chooseEvent():
    events = Events.query.with_entities(Events.name).all()
    eventNames = [event.name for event in events]
    return render_template('chooseEvent.html', events=eventNames)


@bp.route('/chooseProducts', methods=('GET', 'POST'))
def chooseProducts():
    def putEventFeeIfNoProductFee(eventFee, product):
        if not product.service_fee_amount:
            product.service_fee_amount = eventFee
        return product
    if request.method == 'POST':
        sumFee = sum(request.values)
    error = None
    eventName = request.args.get('event')
    event = Events.query.filter_by(name=eventName).first()
    if not event:
        error = "No event was given or event doesn't exist"
        flash(error)
        return redirect(url_for('calculators.chooseEvent'))
    else:
        determineFeeFunc = functools.partial(putEventFeeIfNoProductFee, event.service_fee_amount)
        products = list(map(determineFeeFunc, event.children))
        return render_template('chooseProducts.html', products=products, event=event)
