from application import app
from flask_debugtoolbar import DebugToolbarExtension

app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'sadfjkhsdfxcivckjsdfyawewelk'

toolbar = DebugToolbarExtension(app)
app.run(host='0.0.0.0', port=6001)
