from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages
from views.main import main
from views.blog import blog
from views.about import about

FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'posts'

app = Flask('gale')

#app.config.from_object('config')

app.register_blueprint(main)
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(about, url_prefix='/about')


app.debug = False

app.config.from_object(__name__)
posts = FlatPages(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<path:path>/')
def page(path):
    post = posts.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(port=8000)