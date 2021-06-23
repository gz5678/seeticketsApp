import sqlalchemy
import functools
from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from eventsStore import db
from eventsStore.models import Events

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
        message = "No items were chosen"
        currency = request.form.get('currency')
        if len(request.form) > 1:
            sumFee = 0
            for key in request.form:
                sumFee = sumFee + int(request.form.get(key)) if key != 'currency' else sumFee
            message = f"The fee is {sumFee} {currency}"
        return render_template('showFeeSum.html', message=message)
    error = None
    eventName = request.args.get('event')
    event = Events.query.filter_by(name=eventName).first()
    if not event:
        error = "No event was given or event doesn't exist"
        flash(error)
        return redirect(url_for('calculators.chooseEvent'))
    else:
        determineFeeFunc = functools.partial(putEventFeeIfNoProductFee, event.service_fee_amount)
        products = list(map(determineFeeFunc, event.products))
        return render_template('chooseProducts.html', products=products, event=event)
