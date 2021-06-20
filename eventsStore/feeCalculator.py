from flask import (
    Blueprint, render_template
)
from eventsStore import db

bp = Blueprint('calculators', __name__)

@bp.route('/')
def feeCalculator():
    return render_template('calculators/feeCalculator.html')
