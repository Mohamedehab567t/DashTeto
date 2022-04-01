from Dash import app
from flask import render_template , url_for
from .models import Services

colors={
    'available' : '282828',
    'busy' : '37c837',
    'lock' : 'ffb819'
}

@app.route('/')
def hello():
    s = list(Services.find())
    return render_template('index.html' , s = s , co = colors)