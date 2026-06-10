from flask import Flask

app = Flask(__name__)

from . import catalog, auth

app.register_blueprint(catalog.bp)
app.register_blueprint(auth.bp)

