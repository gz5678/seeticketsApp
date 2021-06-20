from flask import (
    Blueprint, render_template
)
from eventsStore.models import Events

bp = Blueprint('calculators', __name__)

@bp.route('/')
def feeCalculator():
    events = Events.query.all()
    eventNames = [event.name for event in events]
    return render_template('chooseEvent.html', events=eventNames)
