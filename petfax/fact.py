from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

#renders create page
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')