from flask import Blueprint, flash, render_template
live = Blueprint('live', __name__, url_prefix='/live')

@live.route("/",methods=["POST","GET"])
def dash_live():
    return render_template('livedata.html')
