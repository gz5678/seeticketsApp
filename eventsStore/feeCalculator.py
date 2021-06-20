from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from eventsStore import db
from eventsStore.models import Events, Products, association_table

bp = Blueprint('calculators', __name__)


@bp.route('/')
def chooseEvent():
    if request.method == 'POST':
        eventName = request.form['event']
        eventId = Events.query.filter_by(name=eventName).first().id
        productIds = association_table.query.filter_by(event_id=eventId)
        products = Products.query.filter(Products.id.in_(productIds)).all()
        productsNames = [product.name for product in products]
        redirect(url_for('calculators.chooseProducts'))
    events = Events.query.all()
    eventNames = [event.name for event in events]
    return render_template('chooseEvent.html', events=eventNames)
