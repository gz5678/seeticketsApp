from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from eventsStore.models import Events, Products

bp = Blueprint('calculators', __name__)

NO_EVENT_ERROR_MESSAGE = "No event was given or event doesnt exist"
NO_EVENTS_IN_DATABASE_MESSAGE = "Sorry no events are currently available"

@bp.route('/')
def chooseEvent():
    """
    Choose event view which lets the user choose which event to calculate the fee for
    :return: Renders the chooseEvent template
    """
    events = Events.query.with_entities(Events.name).all()
    eventNames = [event.name for event in events]
    # No events in database
    if len(eventNames) == 0:
        flash(NO_EVENTS_IN_DATABASE_MESSAGE)
    return render_template('chooseEvent.html', events=eventNames)


@bp.route('/chooseProducts', methods=('GET', 'POST'))
def chooseProducts():
    """
    A view which lets the user pick the quantity of products he/she wants for the event and calculates the fee
    :return: For GET the chooseProducts template with the relevant products and for POST the total fee
    """
    if request.method == 'POST':
        message = "No items were chosen"
        currency = request.form.get('currency')
        event_service_fee = int(request.form.get('event_service_fee'))
        # We always send currency and event service fee
        if len(request.form) > 2:
            idsList = [key for key in request.form if key not in ['currency', 'event_service_fee']]
            productList = Products.query.filter(Products.id.in_(idsList)).all()
            sumFee = 0
            for product in productList:
                sumFee += _calculate_service_fee(event_service_fee,
                                                 product.service_fee_amount,
                                                 int(request.form.get(str(product.id))))
            message = f"The fee is {sumFee} {currency}"
        return render_template('showFeeSum.html', message=message)

    eventName = request.args.get('event')
    event = Events.query.filter_by(name=eventName).first()
    # Could not find event. Redirecting to same page + error message
    if not event:
        flash(NO_EVENT_ERROR_MESSAGE)
        return redirect(url_for('calculators.chooseEvent'))
    else:
        products = list(event.products)
        return render_template('chooseProducts.html', products=products, event=event)


def _calculate_service_fee(event_service_fee, product_service_fee, quantity):
    """
    Calculates the service fee given the event service fee, product service fee and the quantity of the product
    :param event_service_fee: The event service fee
    :param product_service_fee: The product service fee
    :param quantity: The quantity of the product the user want to buy
    :return: The calculated fee for that product quantity
    """
    # We want to allow 0 service fee
    if product_service_fee or product_service_fee == 0:
        fee = product_service_fee
    else:
        fee = event_service_fee
    return fee * quantity
