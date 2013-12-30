from flask import Flask
from views.main import main
from views.blog import blog
from views.about import about


app = Flask('gale')

#app.config.from_object('config')

app.register_blueprint(main)
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(about, url_prefix='/about')


app.debug = False
