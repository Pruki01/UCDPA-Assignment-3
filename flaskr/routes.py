from flaskr import app

@app.route("/")
def hello_wolrd():
    return "Hello world!"