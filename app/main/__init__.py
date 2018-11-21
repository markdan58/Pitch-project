
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,errors


ERRORS

from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404